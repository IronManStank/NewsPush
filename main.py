#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: main.py

from tools.weather import GetWeather


def main():
    a = GetWeather('北京')
    a.process_url()
    a.get_weather()
    a.pross_weather()
    # pross_weather 不再直接打印结果字符
    # 而是保存在 result_str 中
    print(a.result_str)


if __name__ == '__main__':
    main()
