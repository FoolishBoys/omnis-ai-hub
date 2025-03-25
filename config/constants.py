from enum import IntEnum, unique


@unique
class ChatType(IntEnum):
    # UnKnown = 0  # 未知, 即未设置
    CHATGPT = 2  # ChatGPT

    @staticmethod
    def is_in_chat_types(chat_type: int) -> bool:
        if chat_type in [ChatType.TIGER_BOT.value, ChatType.CHATGPT.value,
                         ChatType.XINGHUO_WEB.value, ChatType.CHATGLM.value,
                         ChatType.BardAssistant.value, ChatType.ZhiPu.value,
                         ChatType.OLLAMA]:
            return True
        return False

    @staticmethod
    def help_hint() -> str:
        return str({member.value: member.name for member in ChatType}).replace('{', '').replace('}', '')
