'''
File Created: Tuesday, 25th March 2025 11:35:58 pm
Author: Csy (1391023795@qq.com)
Description: 
'''
from wcferry import WxMsg
import xml.etree.ElementTree as ET
from robot.robot import Robot


def autoAcceptFriendRequest(self: Robot, msg: WxMsg) -> None:
    try:
        xml = ET.fromstring(msg.content)
        v3 = xml.attrib["encryptusername"]
        v4 = xml.attrib["ticket"]
        scene = int(xml.attrib["scene"])
        self.wcf.accept_new_friend(v3, v4, scene)
    except Exception as e:
        self.LOG.error(f"同意好友出错：{e}")