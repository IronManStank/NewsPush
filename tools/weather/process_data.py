#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: process_data.py

"""
Weather code, converted to text description. 
Wind speed, wind direction, number to text description.
"""


# init datas
class Data:
    # The corresponding relationship between code name and text description.
    WEATHER_DICT = {
        "CLEAR_DAY": "晴天",
        "CLEAR_NIGHT": "晴夜",
        "PARTLY_CLOUDY_DAY": "多云",
        "PARTLY_CLOUDY_NIGHT": "多云",
        "CLOUDY": "阴",
        "RAIN": "雨",
        "SNOW": "雪",
        "WIND": "风",
        "FOG": "雾",
        "HAZE": "霾",
        "SLEET": "冻雨",
    }

    @staticmethod
    def get_wind_direction(wd: float):
        """
        Convert the wind angle to a text description.
        :param wd: Wind angle.
        """
        if wd <= 22.5 or wd > 337.5:
            return "北风"
        elif 22.5 < wd <= 67.5:
            return "东北风"
        elif 67.5 < wd <= 112.5:
            return "东风"
        elif 112.5 < wd <= 157.5:
            return "东南风"
        elif 157.5 < wd <= 202.5:
            return "南风"
        elif 202.5 < wd <= 247.5:
            return "西南风"
        elif 247.5 < wd <= 292.5:
            return "西风"
        elif 292.5 < wd <= 337.5:
            return "西北风"
        else:
            return "未知"

    @staticmethod
    def get_wind_speed(ws: float):
        """
        Convert wind speed numbers to text descriptions.
        :param ws: Wind speed.
        """
        if ws <= 2:
            return "无风"
        if 2 < ws <= 6:
            return "软风"
        elif 6 < ws <= 12:
            return "轻风"
        elif 12 < ws <= 19:
            return "缓风"
        elif 19 < ws <= 30:
            return "和风"
        elif 30 < ws <= 40:
            return "清风"
        elif 40 < ws <= 51:
            return "强风"
        elif 51 < ws <= 62:
            return "疾风"
        elif 62 < ws <= 75:
            return "烈风"
        elif 75 < ws <= 87:
            return "增强烈风"
        elif 87 < ws <= 103:
            return "暴风"
        elif 103 < ws <= 149:
            return "台风"
        elif 149 < ws <= 183:
            return "强台飓风"
        elif 183 < ws <= 220:
            return "超强台飓风"
        else:
            return "极强台飓风"
