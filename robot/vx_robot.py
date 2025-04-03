# -*- coding: utf-8 -*-

import os
from config.configuration import Config
import logging
import re
import time

from queue import Empty
from threading import Thread
import xml.etree.ElementTree as ET

from wcferry import Wcf
from base.wechatferry_plugin.WxMsg_impl import WxMsgImpl
from base.func_coze import CozeClient
from job_mgmt import Job
from robot.Wechat.msg_types import MsgTypes as m_t

from base.old_func.func_chengyu import cy
from base.old_func.func_weather import Weather
from base.old_func.func_news import News


__version__ = "39.2.4.0"
__core__ = "0.1"


class VX_Robot(Job):
    """个性化自己的机器人
    """

    def __init__(self, config: Config, wcf: Wcf, chat_type: int) -> None:
        self.wcf = wcf
        self.config = config
        self.LOG = logging.getLogger("VX_Robot")
        
        self.pre_init()
        
        self.wxid = None
        self.allContacts = None
        self.chat = None
        self.vx_data_init()
        self.coze_init()
        
        self._msg_timestamps = []
    
    @property
    def msg_func_map(self) -> dict:
        return {
            m_t.TEXT: self.toChitchat,
            m_t.VOICE: self.voice_msg
        }
        

    def pre_init(self):
        self.GROUPS = self.config.get_config_by_key("groups")["enable"]
        self.SEND_RATE_LIMIT = self.config.get_config_by_key("send_rate_limit", 0)
        self.PROJ_ROOT_PATH = self.config.get_config_by_key("ProjRootPath")
        self.Temp_Media_Path = os.path.join(self.PROJ_ROOT_PATH, "TempMedia")
        
        if not os.path.exists(self.Temp_Media_Path):
            os.makedirs(self.Temp_Media_Path)


    def vx_data_init(self):
            # 用户id或群聊id
            self.wxid = self.wcf.get_self_wxid()
            self.allContacts = self.getAllContacts()
            self.LOG.error(f"{self.wcf.get_msg_types()}")
    
    
    def coze_init(self):
        self.chat = CozeClient(self.config.get_config_by_key("coze"))
        self.LOG.info(f"已选择: {self.chat}")


    def sendTextMsg(self, msg: str, receiver: str, at_list: str = "") -> None:
        """ 发送消息
        :param msg: 消息字符串
        :param receiver: 接收人wxid或者群id
        :param at_list: 要@的wxid, @所有人的wxid为：notify@all
        """
        # 随机延迟0.3-1.3秒，并且一分钟内发送限制
        time.sleep(float(str(time.time()).split('.')[-1][-2:]) / 100.0 + 0.3)
        now = time.time()
        if self.SEND_RATE_LIMIT > 0:
            # 清除超过1分钟的记录
            self._msg_timestamps = [t for t in self._msg_timestamps if now - t < 60]
            if len(self._msg_timestamps) >= self.SEND_RATE_LIMIT:
                self.LOG.warning("发送消息过快，已达到每分钟"+self.SEND_RATE_LIMIT+"条上限。")
                return
            self._msg_timestamps.append(now)

        # msg 中需要有 @ 名单中一样数量的 @
        ats = ""
        if at_list:
            if at_list == "notify@all":  # @所有人
                ats = " @所有人"
            else:
                wxids = at_list.split(",")
                for wxid in wxids:
                    # 根据 wxid 查找群昵称
                    ats += f" @{self.wcf.get_alias_in_chatroom(wxid, receiver)}"

        # {msg}{ats} 表示要发送的消息内容后面紧跟@，例如 北京天气情况为：xxx @张三
        if ats == "":
            self.LOG.info(f"To {receiver}: {msg}")
            self.wcf.send_text(f"{msg}", receiver, at_list)
        else:
            self.LOG.info(f"To {receiver}: {ats}\r{msg}")
            self.wcf.send_text(f"{ats}\n\n{msg}", receiver, at_list)


    def getAllContacts(self) -> dict:
        """
        获取联系人（包括好友、公众号、服务号、群成员……）
        格式: {"wxid": "NickName"}
        """
        contacts = self.wcf.query_sql("MicroMsg.db", "SELECT UserName, NickName FROM Contact;")
        self.LOG.info(f"获取联系人: {contacts}")
        return {contact["UserName"]: contact["NickName"] for contact in contacts}

    
    def toAt(self, msg: WxMsgImpl) -> bool:
        """处理被 @ 消息
        :param msg: 微信消息结构
        :return: 处理状态，`True` 成功，`False` 失败
        """
        return self.toChitchat(msg)


    def toChitchat(self, msg: WxMsgImpl) -> bool:
        """闲聊，接入 ChatGPT
        """
        if not self.chat:  # 没接
            rsp = "你@我干嘛？"
        else:  # 接了 
            self.LOG.error(f"===========获取vx消息: {msg.content}")
            question = re.sub(r"@.*?[\u2005|\s]", "", msg.content).replace(" ", "")
            self.LOG.error(f"===========提取的内容: {question}")
            rsp = self.chat.get_answer(question, (msg.roomid if msg.from_group() else msg.sender))

        if rsp:
            if msg.from_group():
                self.sendTextMsg(rsp, msg.roomid, msg.sender)
            else:
                self.sendTextMsg(rsp, msg.sender)

            return True
        else:
            self.LOG.error(f"===========toChitchat闲聊出现问题")
            return False
    
    def voice_msg(self, msg: WxMsgImpl) -> bool:
        """_summary_
        语音处理回复
        """
        path = self.wcf.get_audio_msg(msg.id, self.Temp_Media_Path)
        self.LOG.error(f"===========语音路径：{path}")

    
    # 主入口处理消息
    def enableReceivingMsg(self) -> None:
        def innerProcessMsg(wcf: Wcf):
            while wcf.is_receiving_msg():
                try:
                    msg = wcf.get_msg()
                    self.LOG.info(msg)
                    # 非自己的内容
                    if not msg.from_self():
                        # 群聊
                        if msg.from_group():
                            self.processGroupMsg(msg)
                        # 单聊
                        else:
                            self.processMsg(msg)
                    
                except Empty:
                    continue  # Empty message
                except Exception as e:
                    self.LOG.error(f"Receiving message error: {e}")

        self.wcf.enable_receiving_msg()
        Thread(target=innerProcessMsg, name="GetMessage", args=(self.wcf,), daemon=True).start()


    def processMsg(self, msg: WxMsgImpl):
        """
        单聊
        """
        func_ = self.msg_func_map.get(msg.type, None)
        func_(msg)
          
          
    def processGroupMsg(self, msg: WxMsgImpl):
        """
        群聊
        """
        if msg.is_at(self.wxid):  # 被@
            self.processMsg(msg)


    def keepRunningAndBlockProcess(self) -> None:
        """
        保持机器人运行，不让进程退出
        """
        while True:
            self.runPendingJobs()
            time.sleep(1)


    # def autoAcceptFriendRequest(self, msg: WxMsgImpl) -> None:
    #     try:
    #         xml = ET.fromstring(msg.content)
    #         v3 = xml.attrib["encryptusername"]
    #         v4 = xml.attrib["ticket"]
    #         scene = int(xml.attrib["scene"])
    #         self.wcf.accept_new_friend(v3, v4, scene)
    #     except Exception as e:
    #         self.LOG.error(f"同意好友出错：{e}")

    # def sayHiToNewFriend(self, msg: WxMsgImpl) -> None:
    #     nickName = re.findall(r"你已添加了(.*)，现在可以开始聊天了。", msg.content)
    #     if nickName:
    #         # 添加了好友，更新好友列表
    #         self.allContacts[msg.sender] = nickName[0]
    #         self.sendTextMsg(f"Hi {nickName[0]}，我自动通过了你的好友请求。", msg.sender)

    # def newsReport(self) -> None:
    #     receivers = self.config.NEWS
    #     if not receivers:
    #         return

    #     news = News().get_important_news()
    #     for r in receivers:
    #         self.sendTextMsg(news, r)

    # def weatherReport(self) -> None:
    #     receivers = self.config.WEATHER
    #     if not receivers or not self.config.CITY_CODE:
    #         self.LOG.warning("未配置天气城市代码或接收人")
    #         return

    #     report = Weather(self.config.CITY_CODE).get_weather()
    #     for r in receivers:
    #         self.sendTextMsg(report, r)

        # def toChengyu(self, msg: WxMsgImpl) -> bool:
    
    #     """
    #     处理成语查询/接龙消息
    #     :param msg: 微信消息结构
    #     :return: 处理状态，`True` 成功，`False` 失败
    #     """
    #     status = False
    #     texts = re.findall(r"^([#?？])(.*)$", msg.content)
    #     # [('#', '天天向上')]
    #     if texts:
    #         flag = texts[0][0]
    #         text = texts[0][1]
    #         if flag == "#":  # 接龙
    #             if cy.isChengyu(text):
    #                 rsp = cy.getNext(text)
    #                 if rsp:
    #                     self.sendTextMsg(rsp, msg.roomid)
    #                     status = True
    #         elif flag in ["?", "？"]:  # 查词
    #             if cy.isChengyu(text):
    #                 rsp = cy.getMeaning(text)
    #                 if rsp:
    #                     self.sendTextMsg(rsp, msg.roomid)
    #                     status = True

    #     return status
