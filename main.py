#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: main.py

from tools.weather import get_weather_str
import argparse


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

    weather_str = get_weather_str('北京', args['token'][0])

    print(weather_str)


if __name__ == '__main__':
    main()
