#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: process_data.py
import requests
import re
from retry import retry


class GetWeatherReport(object):
    def __init__(self) -> None:
        self.city_file_path = r"./assets/weatherdata/city_data.csv"
        self.city_code = self.get_city_code("北京")
        self.data = None
        
    @retry(tries=3, delay=2)
    def get_weather_tm(self):
        try:
            weather_url = (
                f"http://t.weather.sojson.com/api/weather/city/{self.city_code}"
            )
            req = requests.get(weather_url, timeout=5)
            if req.status_code == 200:
                return req.json()
        except Exception as e:
            print(f"天气详细获取失败，可能是网络问题:, {e}")
            return None


    def get_city_code(self, city_name):
        try:
            with open(self.city_file_path , "r", encoding="utf-8") as f:
                for line in f.readlines():
                    if city_name in line:
                        # print(line)
                        return line.split(",")[0]
        except Exception as e:
            print(f"城市代码获取失败，可能路径错误:, {e}")

    def weather_meassage(self, city: str):
        try:
            self.city_code = self.get_city_code(city)
            # print(self.city_code)
            self.data = self.get_weather_tm()
            if self.data is not None:
                city = self.data["cityInfo"]["city"]
                forcast = self.data["data"]["forecast"][1]
                low = re.findall(r"\d+", forcast["low"])[0]
                high = re.findall(r"\d+", forcast["high"])[0]
                message = (
                    forcast["ymd"]
                    + "，"
                    + f"{city}明天气温"
                    + f"{low}~{high}℃，"
                    + forcast["type"]
                    + "，"
                    + forcast["fx"]
                    + forcast["fl"]
                    + "，"
                    + forcast["notice"]
                    + "\n"
                )
                print(message)
                return message
            else:
                print("天气信息获取失败")
                return None
        except Exception as e:
            print(f"天气信息生成失败，问题如下: {e}")
            return None
        

if __name__ == "__main__":
    weather = GetWeatherReport()
    weather.weather_meassage("苏州")
