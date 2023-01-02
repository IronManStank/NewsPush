#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: main.py

from tools.weather import get_weather_str
import argparse
from tools.emailpush import send_email, get_email_info
from NewsService import GetNews


def get_cli_args():
    # 在这里解析命令行
    parser = argparse.ArgumentParser(description="NewsPush Bot")

    parser.add_argument('--token',  '-t', type=str,
                        default=['token.txt'], help='token本身，或者所在的txt文件路径', nargs=1)

    # 邮件相关
    # 用这里提供的参数去更新本地文件的参数
    # 这里的参数可以不是完整的
    # 如果本地配置文件中有完整参数，那么这些参数完全可以不提供
    parser.add_argument('--sender', '-s', type=str,
                        required=False, help='email: sender', nargs=1)

    parser.add_argument('--etoken', '-n', type=str,
                        required=False, help='email: token', nargs=1)

    parser.add_argument('--receivers', '-r', type=str,
                        required=False, help='email: 接收者，多个接收者用 , 隔开', nargs=1)

    parser.add_argument('--hfrom', '-f', type=str,
                        required=False, help='email: HeaderFrom', nargs=1)

    parser.add_argument('--hto', '-o', type=str,
                        required=False, help='email: HeaderTo', nargs=1)

    parser.add_argument('--subject', '-j', type=str,
                        required=False, help='email: subject', nargs=1)

    parser.add_argument('--message', '-m', type=str,
                        required=False, help='email: message 可以是文件路径', nargs=1)

    args = parser.parse_args()._get_kwargs()

    args = {x: y for x, y in args}

    # 现在 args 是个字典
    print(args)

    return args


def main():
    args = get_cli_args()
    weather_str = '未找到天气数据'
    try:
        weather_str = get_weather_str('北京', args['token'][0])
        print(weather_str)
    except Exception as e:
        print(f'获取天气信息失败: {e}')

    # 获取新闻
    try:
        News = GetNews()
        News.get_page()
        news_info = News.process_page()

        News.generate_html_file(
            'NewsTempelate.html', 'News.html', weather_str, news_info)
    except Exception as e:
        print(f'获取新闻信息失败: {e}')

    # 获取生成的新闻html文件
    try:
        with open('News.html', 'r', encoding='utf-8') as f:
            news_str = f.read()
    except Exception as e:
        news_str = e
        print(f'获取新闻html文件内容失败: {e}')

    # 发送邮件
    info = get_email_info(args)

    try:
        send_email(info, news_str)

    except Exception as e:
        print(f'发送失败: Err: {e}')
        raise e


if __name__ == '__main__':
    main()
