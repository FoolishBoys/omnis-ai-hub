'''
File Created: Tuesday, 25th March 2025 11:24:27 pm
Author: Csy (1391023795@qq.com)
Description: 
'''

import re
from wcferry import WxMsg

from robot.robot import Robot


def sayHiToNewFriend(self: Robot, msg: WxMsg) -> None:
    nickName = re.findall(r"你已添加了(.*)，现在可以开始聊天了。", msg.content)
    if nickName:
        # 添加了好友，更新好友列表
        self.allContacts[msg.sender] = nickName[0]
        self.sendTextMsg(f"Hi {nickName[0]}，我自动通过了你的好友请求。", msg.sender)