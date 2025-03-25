from enum import IntEnum, unique


@unique
class ChatType(IntEnum):
    # UnKnown = 0  # 未知, 即未设置
    # CHATGPT = 2  # ChatGPT

    @staticmethod
    def help_hint() -> str:
        return str({member.value: member.name for member in ChatType}).replace('{', '').replace('}', '')
