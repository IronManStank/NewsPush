#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: main.py

from tools.weather import get_weather_str
import argparse
from tools.emailservice.EmailPushService import send_email


def get_cli_args():
    # 在这里解析命令行
    parser = argparse.ArgumentParser(description="NewsPush Bot")

    parser.add_argument('--token',  '-t', type=str,
                        default=['token.txt'], help='token本身，或者所在的txt文件路径', nargs=1)

    args = parser.parse_args()._get_kwargs()

    args = {x: y for x, y in args}

    # 现在 args 是个字典
    # print(args)

    return args


def main():
    args = get_cli_args()

    try:
        weather_str = get_weather_str('北京', args['token'][0])

        print(weather_str)
    except Exception as e:
        print(f'获取天气信息失败: {e}')

    # 发送邮件
    info = {
        'sender': '1157723200@qq.com',
        'token': 'mqrsefodflqejcji',
        'receivers': ['1157723200@qq.com', 'azureqaq@icloud.com'],
        'header': {'HeaderFrom': 'Personal Intelligence System', 'HeaderTo': 'BOSS'},
        'subject': 'Email test',
        'message': 'This is a test email.'
    }
    try:
        send_email(info, 'test.html')
    except Exception as e:
        print(f'发送失败: Err: {e}')
        raise e


if __name__ == '__main__':
    main()
