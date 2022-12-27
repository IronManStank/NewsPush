#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: main.py

from tools.weather import GetWeather
import argparse

# 在这里解析命令行
def get_cli_args():
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

    a = GetWeather('北京', args['token'][0])
    a.process_url()
    a.get_weather()
    a.pross_weather()
    # pross_weather 不再直接打印结果字符
    # 而是保存在 result_str 中
    print(a.result_str)


if __name__ == '__main__':
    main()
