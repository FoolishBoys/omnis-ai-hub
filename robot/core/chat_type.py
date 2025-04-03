'''
File Created: Thursday, 3rd April 2025 4:17:04 pm
Author: Csy (1391023795@qq.com)
Description: 
'''
from enum import Enum, IntEnum, unique


@unique
class ChatType(IntEnum):
    # UnKnown = 0  # 未知, 即未设置
    # CHATGPT = 2  # ChatGPT

    @staticmethod
    def help_hint() -> str:
        return str({member.value: member.name for member in ChatType}).replace('{', '').replace('}', '')
