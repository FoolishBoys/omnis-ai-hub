'''
File Created: Monday, 24th March 2025 9:46:13 am
Author: Csy (1391023795@qq.com)
Description: 
'''

import logging.config
from config.logc import log_config
# 初始化日志配置
logging.config.dictConfig(log_config)
logger = logging.getLogger()

import signal
from config.configuration import Config
from argparse import ArgumentParser
from base.func_report_reminder import ReportReminder
from config.constants import ChatType
from robot.robot import Robot, __core__
from wcferry import Wcf


def main(chat_type: int):
    
    
    config = Config()
    
    wcf = Wcf(debug=True)

    def handler(sig, frame):
        wcf.cleanup()  # 退出前清理环境
        exit(0)

    signal.signal(signal.SIGINT, handler)

    robot = Robot(config, wcf, chat_type)
    robot.LOG.info(f"Omnis Ai Hub >>【{__core__}】成功启动···")

    # 机器人启动发送测试消息
    robot.sendTextMsg("机器人启动成功！", "filehelper")

    # 接收消息
    # robot.enableRecvMsg()     # 可能会丢消息？
    robot.enableReceivingMsg()  # 加队列

    # 每天 7 点发送天气预报
    robot.onEveryTime("07:00", robot.weatherReport)

    # 每天 7:30 发送新闻
    robot.onEveryTime("07:30", robot.newsReport)

    # 每天 16:30 提醒发日报周报月报
    robot.onEveryTime("16:30", ReportReminder.remind, robot=robot)

    # 让机器人一直跑
    robot.keepRunningAndBlockProcess()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-c', type=int, default=0, help=f'选择模型参数序号: {ChatType.help_hint()}')
    args = parser.parse_args().c
    main(args)
