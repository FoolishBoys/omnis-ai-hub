from enum import Enum, IntEnum, unique


@unique
class ChatType(IntEnum):
    # UnKnown = 0  # 未知, 即未设置
    # CHATGPT = 2  # ChatGPT

    @staticmethod
    def help_hint() -> str:
        return str({member.value: member.name for member in ChatType}).replace('{', '').replace('}', '')


class MsgTypes(Enum):
    """_summary_
    0	朋友圈消息
    1	文字
    3	图片
    34	语音
    37	好友确认
    40	POSSIBLEFRIEND_MSG
    42	名片
    43	视频
    47	石头剪刀布 或 表情图片
    48	位置
    49	共享实时位置、文件、转账、链接
    50	VOIPMSG
    51	微信初始化
    52	VOIPNOTIFY
    53	VOIPINVITE
    62	小视频
    66	微信红包
    9999	SYSNOTICE
    10000	红包、系统消息
    10002	撤回消息
    1048625	搜狗表情
    16777265	链接
    436207665	微信红包
    536936497	红包封面
    754974769	视频号视频
    771751985	视频号名片
    822083633	引用消息
    922746929	拍一拍
    973078577	视频号直播
    974127153	商品链接
    975175729	视频号直播
    1040187441	音乐链接
    1090519089	文件
    Args:
        Enum (_type_): _description_
    """
    # 朋友圈消息
    WECHAT_MOMENTS = 0
    # 文字
    TEXT = 1
    # 图片
    IMAGE = 3
    # 语音
    VOICE = 34
    # 好友确认
    FRIEND_CONFIRM = 37
    # POSSIBLEFRIEND_MSG
    POSSIBLEFRIEND_MSG = 40
    # 名片
    CARD = 42
    # 视频
    VIDEO = 43
    # 石头剪刀布 或 表情图片
    STONE_SCISSORS_CLIP = 47
    # 位置
    LOCATION = 48
    # 共享实时位置、文件、转账、链接
    SHARE_LOCATION_FILE_TRANSFER_LINK = 49
    # VOIPMSG
    VOIPMSG = 50
    # 微信初始化
    WECHAT_INIT = 51
    # VOIPNOTIFY
    VOIPNOTIFY = 52
    # VOIPINVITE
    VOIPINVITE = 53
    # 小视频
    SMALL_VIDEO = 62
    # 微信红包
    WECHAT_RED_PACKET = 66
    # SYSNOTICE
    SYSNOTICE = 9999
    # 红包、系统消息
    RED_PACKET_SYS_NOTICE = 10000
    # 撤回消息
    RECALL = 10002
    # 搜狗表情
    SOUGOU_EMOJI = 1048625
    # 链接
    LINK = 16777265
    # 微信红包
    WECHAT_RED_PACKET_2 = 436207665
    # 红包封面
    RED_PACKET_COVER = 536936497
    # 视频号视频
    VIDEO_NUMBER_VIDEO = 754974769
    # 视频号名片
    VIDEO_NUMBER_CARD = 771751985
    # 引用消息
    QUOTE_MESSAGE = 822083633
    # 拍一拍
    PAT_ONE_PAT = 922746929
    # 视频号直播
    VIDEO_NUMBER_LIVE = 973078577
    # 商品链接
    PRODUCT_LINK = 974127153
    # 视频号直播
    VIDEO_NUMBER_LIVE_2 = 975175729
    # 音乐链接
    MUSIC_LINK = 1040187441
    # 文件
    FILE = 1090519089
    
    