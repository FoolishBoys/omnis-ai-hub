#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from datetime import datetime

import httpx
from cozepy import COZE_CN_BASE_URL, COZE_COM_BASE_URL, MessageRole
from cozepy import Coze, TokenAuth, Message, ChatStatus  


class CozeClient():
    """_summary_
    Authentication: pat_Jxxx
    Area: cn
    bot: 
    - botid: 123
      botname: 123
    - botid: 1234
      botname: 1234
    """

    def __init__(self, conf: dict) -> None:
        self.LOG = logging.getLogger("Coze")
        self.api = COZE_CN_BASE_URL if conf.get("Area") in COZE_CN_BASE_URL else COZE_COM_BASE_URL
        # Todo: 2.bot改字典
        self.bot_list = conf.get("bot")
        
        # 初始化Coze客户端
        self.client = Coze(auth=TokenAuth(token=conf.get("Authentication")), base_url=self.api)
            
        self.conversation_list = {}

    def __repr__(self):
        return 'CozeClient'

    def get_answer(self, question: str, wxid: str, bot_id=None) -> str:
        # wxid或者roomid,个人时为微信id，群消息时为群id
        self.updateMessage(wxid, question, MessageRole.USER)
        concatenated_content = ""
        try:
            # 调用Coze API
            chat_poll = self.client.chat.create_and_poll(
                bot_id="7485651387741765666",  # 使用model作为bot_id
                user_id=wxid,
                additional_messages=self.conversation_list[wxid]
            )

            
            # concatenated_content = "".join(message.content for message in chat_poll.messages)
            for message in chat_poll.messages:
                self.LOG.error(f"=============返回消息内容：{message.content}")
                if "generate_answer_finish" in message.content:
                    break
                concatenated_content+=message.content
                
            
            self.LOG.error(f"=============完整消息内容：{concatenated_content}")
                 
            if chat_poll.chat.status == ChatStatus.COMPLETED:
                self.LOG.error(f"=============本次token：{chat_poll.chat.usage.token_count}")
            
            self.updateMessage(wxid, concatenated_content, MessageRole.ASSISTANT)
            
        except Exception as e:
            self.LOG.error(f"获取coze回信时，发生未知错误：{str(e)}")
            concatenated_content = "抱歉，获取coze回信时，发生了一些错误，请稍后再试（机器人回复）"

        return concatenated_content

    # Todo: 4.通用代码 更新消息记录
    def updateMessage(self, wxid: str, content: str, role) -> None:
        now_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # time_mk = "当需要回答时间时请直接参考回复:"
        # 初始化聊天记录,组装系统信息
        if wxid not in self.conversation_list.keys():
            
            self.conversation_list[wxid] = []

        # 当前问题
        if role == MessageRole.USER:
            self.conversation_list[wxid].append(
                Message.build_user_question_text(content)
            )
        else:
            self.conversation_list[wxid].append(
                Message.build_assistant_answer(content)
            )

        self.LOG.error(f"==========更新消息后的消息列表：{self.conversation_list[wxid]}")
        # 只存储10条记录，超过滚动清除
        i = len(self.conversation_list[wxid])
        # Todo: 3.记忆空间由配置调整
        if i > 10:
            print("滚动清除微信记录：" + wxid)
            # 删除多余的记录，倒着删，且跳过第一个的系统消息
            del self.conversation_list[wxid][1]


if __name__ == "__main__":
    from config.configuration import Config
    config = Config()
    if not config:
        exit(0)

    chat = CozeClient(config.get_config_by_key("coze"))

    while True:
        q = input(">>> ")
        try:
            time_start = datetime.now()  # 记录开始时间
            print(chat.get_answer(q, "wxid"))
            time_end = datetime.now()  # 记录结束时间

            print(f"{round((time_end - time_start).total_seconds(), 2)}s")  # 计算的时间差为程序的执行时间，单位为秒/s
        except Exception as e:
            print(e)
