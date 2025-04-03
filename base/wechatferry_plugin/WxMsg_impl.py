'''
File Created: Thursday, 3rd April 2025 11:10:11 am
Author: Csy (1391023795@qq.com)
Description: 
'''

from wcferry import WxMsg
from datetime import datetime

class WxMsgImpl(WxMsg):
    """重写了 `__str__` 方法
    """

    def __str__(self) -> str:
        """重写了 `__str__` 方法，返回消息的字符串表示
        """
        s = f"{'自己发的:' if self._is_self else ''}"
        s += f"{self.sender}[{self.roomid}]|{self.id}|{datetime.fromtimestamp(self.ts)}|{self.type}|{self.sign}"
        s += f"消息类型格式XML内容：\n{self.xml.replace(chr(10), '').replace(chr(9),'')}\n"
        s += f"主体消息：\n{self.content}"
        s += f"Thumb:\n{self.thumb if self.thumb else "?"}"
        s += f"Extra:\n{self.extra if self.extra else "?"}" 
        return s