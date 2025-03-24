#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from datetime import datetime

import httpx
from cozepy import Coze, TokenAuth, Message, COZE_CN_BASE_URL


class CozeTest():
    def __init__(self, conf: dict) -> None:
        key = conf.get("key")
        # Todo: 1.国外使用
        api = COZE_CN_BASE_URL
        # proxy = conf.get("proxy")
        prompt = conf.get("prompt")
        # Todo: 2.model改为选填
        self.model = conf.get("model")
        self.LOG = logging.getLogger("CozeTest")
        
        # 初始化Coze客户端
        self.client = Coze(auth=TokenAuth(token=key), base_url=api)
            
        self.conversation_list = {}
        self.system_content_msg = {"role": "system", "content": prompt}

    def __repr__(self):
        return 'CozeTest'

    def get_answer(self, question: str, wxid: str) -> str:
        # wxid或者roomid,个人时为微信id，群消息时为群id
        self.updateMessage(wxid, question, "user")
        rsp = ""
        try:
            # 构建消息列表
            messages = self.conversation_list[wxid]
            
            # 调用Coze API
            chat_poll = self.client.chat.create_and_poll(
                bot_id=self.model,  # 使用model作为bot_id
                user_id=wxid,
                additional_messages=[
                    Message.build_user_question_text(msg["content"]) if msg["role"] == "user" 
                    else Message.build_assistant_answer(msg["content"]) 
                    for msg in messages[1:]
                ]  # 跳过system消息
            )
            
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
    config = Config().CHATGPT
    if not config:
        exit(0)

    chat = CozeTest(config)

    while True:
        q = input(">>> ")
        try:
            time_start = datetime.now()  # 记录开始时间
            print(chat.get_answer(q, "wxid"))
            time_end = datetime.now()  # 记录结束时间

            print(f"{round((time_end - time_start).total_seconds(), 2)}s")  # 计算的时间差为程序的执行时间，单位为秒/s
        except Exception as e:
            print(e)

#chatgpt:
#  key: 你的Coze API Token
#  api: https://api.coze.cn
#  model: 你的Bot ID
