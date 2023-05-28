#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# file: main.py

import argparse

from tools.emailpush import update_from_cline_info, send_email
from tools.newsservice import GetNews
from tools.weather import get_weather_str,GetWeatherReport


def get_cli_args():
    # Parse the command line here.
    parser = argparse.ArgumentParser(description="NewsPush Bot")

    parser.add_argument('--token',  '-t', type=str,
                        default=['token.txt'], help='token本身，或者所在的txt文件路径', nargs=1)

# Email Related.
# Update the local file parameters with the parameters provided here.
# The  parameter may not be complete.
# If there are full parameters in the local configuration file, then these parameters may not be supplied at all.
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

    parser.add_argument('--city', '-c', type=str, default="南开",
                        required=False, help='天气选择的位置', nargs=1)

    args = parser.parse_args()._get_kwargs()

    args = {x: y for x, y in args}

    # Args：dict type.
    print(args)

    return args


def main():
    # Get Weather Info
    args = get_cli_args()
    weather_str = '未找到天气数据'
    try:
        weather = GetWeatherReport()
        weather_str=weather.weather_meassage(args['city'][0])
        print(weather_str)
    except Exception as e:
        print(f'第一种方法获取天气失败: {e}' + ",尝试使用第二种方法获取天气信息")
        try:
            weather_str = get_weather_str(args['city'][0], args['token'][0])
            print(weather_str)
        except Exception as e:           
            print(f'获取天气信息失败: {e}')

    # Get News Info
    try:
        News = GetNews()
        News.get_page()
        news_info = News.process_page()

        News.generate_html_file(
            'NewsTempelate.html', 'News.html', weather_str, news_info)
    except Exception as e:
        print(f'获取新闻信息失败: {e}')

    # Generate News HTML File
    try:
        with open('News.html', 'r', encoding='utf-8') as f:
            news_str = f.read()
    except Exception as e:
        
        print(f'获取新闻html文件内容失败: {e}')
        raise e

    # Send Email
    info = update_from_cline_info(args)

    try:
        send_email(info, news_str)

    except Exception as e:
        print(f'发送失败: Err: {e}')
        raise e


if __name__ == '__main__':
    main()
