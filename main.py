#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: main.py

from tools.weather import GetWeather
from tools.weather.get_token import get_token
import argparse


def main():
    parser = argparse.ArgumentParser(description="NewsPush Bot")

    parser.add_argument('--token',  '-t', type=str,
                        default=['token.txt'], help='token本身，或者所在的txt文件路径', nargs=1)

    args = parser.parse_args()._get_kwargs()

    args = {x: y for x, y in args}

    # 现在 args 是个字典
    print(args)

    token = get_token(args['token'][0])


    a = GetWeather('北京', token)
    a.process_url()
    a.get_weather()
    a.pross_weather()
    # pross_weather 不再直接打印结果字符
    # 而是保存在 result_str 中
    print(a.result_str)


if __name__ == '__main__':
    main()
