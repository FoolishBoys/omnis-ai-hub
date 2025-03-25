#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from datetime import datetime
import os
import time

import httpx
from cozepy import COZE_CN_BASE_URL, COZE_COM_BASE_URL
from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageContentType  


class Coze():
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
        self.auth = conf.get("Authentication")
        self.api = COZE_CN_BASE_URL if conf.get("Area") in COZE_CN_BASE_URL else COZE_COM_BASE_URL
        # Todo: 2.bot改字典
        self.bot_list = conf.get("bot")
        
        # 初始化Coze客户端
        self.client = Coze(auth=TokenAuth(token=self.auth), base_url=self.api)
            
        self.conversation_list = {}

    def __repr__(self):
        return 'Coze'

    def get_answer(self, question: str, wxid: str, bot_id) -> str:
        # wxid或者roomid,个人时为微信id，群消息时为群id
        self.updateMessage(wxid, question, "user")
        rsp = ""
        try:
            # 构建消息列表
            messages = self.conversation_list[wxid]
            
            # 调用Coze API
            chat_poll = self.client.chat.create_and_poll(
                bot_id=bot_id,  # 使用model作为bot_id
                user_id=wxid,
                additional_messages=[
                    Message.build_user_question_text("Hello?123"),
                ]  
            )
            '''
                for message in chat_poll.messages:
                     print(message.content, end="", flush=True)

                if chat_poll.chat.status == ChatStatus.COMPLETED:
                    print()
                    print("token usage:", chat_poll.chat.usage.token_count)
            '''
            
            # 获取回复
            if chat_poll.chat.status == "completed":
                for message in chat_poll.messages:
                    if message.role == "assistant" and message.type == "answer":
                        rsp = message.content
                        break
                
                if not rsp:
                    rsp = "抱歉，我现在无法回答这个问题。"
            else:
                rsp = "抱歉，服务暂时不可用，请稍后再试。"
                
            rsp = rsp[2:] if rsp.startswith("\n\n") else rsp
            rsp = rsp.replace("\n\n", "\n")
            self.updateMessage(wxid, rsp, "assistant")
            
        except Exception as e0:
            self.LOG.error(f"发生未知错误：{str(e0)}")
            rsp = "抱歉，发生了一些错误，请稍后再试。"

        return rsp

    # Todo: 4.通用代码 更新消息记录
    def updateMessage(self, wxid: str, question: str, role: str) -> None:
        now_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # time_mk = "当需要回答时间时请直接参考回复:"
        # 初始化聊天记录,组装系统信息
        if wxid not in self.conversation_list.keys():
            question_ = [
                self.system_content_msg,
                # {"role": "system", "content": "" + time_mk + now_time}
            ]
            self.conversation_list[wxid] = question_

        # 当前问题
        self.conversation_list[wxid].append(
            {"role": role, "content": question}
        )

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

    chat = Coze(config.get_config_by_key("coze"))

    while True:
        q = input(">>> ")
        try:
            time_start = datetime.now()  # 记录开始时间
            print(chat.get_answer(q, "wxid"))
            time_end = datetime.now()  # 记录结束时间

            print(f"{round((time_end - time_start).total_seconds(), 2)}s")  # 计算的时间差为程序的执行时间，单位为秒/s
        except Exception as e:
            print(e)
