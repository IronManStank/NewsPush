#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: weather.py


import requests
from tools.weather.process_data import Data
from tools.weather.citytodata import CitytoData
from tools.error import GetWeatherFaildError
from tools.weather.get_token import get_token


class GetWeather(object):
    def __init__(self, city):
        self.baseurl = 'https://api.caiyunapp.com/v2.6'
        self.city = city
        self.loacation = CitytoData(self.city).get_data()
        self.dailysteps = 1
        self.info_dict = {
            'token': get_token(),
            'city': self.loacation,
            'forcastype': 'daily',
            'ASKPARAM': {
                'dailysteps': self.dailysteps,
                'alert': 'true'
            }
        }

        self.askurl = ''
        self.weatherInfo = {}

        # 保存结果
        self.result_str = ''

    def process_url(self):
        '''处理url'''
        # "https://api.caiyunapp.com/v2.6/TAkhjf8d1nlSlspN/101.6656,39.2072/daily?dailysteps=1"
        self.askurl = self.baseurl + '/' + \
            self.info_dict['token'] + '/'+self.info_dict['city'] + \
            '/' + self.info_dict['forcastype']

    def get_weather(self):
        try:
            r = requests.get(
                self.askurl, params=self.info_dict['ASKPARAM'])
            self.weatherInfo = r.json()
        except Exception as e:
            print('获取天气失败')
            raise GetWeatherFaildError(f'获取天气失败, {e}')

    def pross_weather(self):
        weather = self.weatherInfo
        temperature = weather['result']['daily']['temperature'][0]
        wind = weather['result']['daily']['wind'][0]
        air_quality = weather['result']['daily']['air_quality']
        skycon = weather['result']['daily']['skycon'][0]
        precipitation = weather['result']['daily']['precipitation'][0]
        life_index = weather['result']['daily']['life_index']
        ultraviolet = life_index['ultraviolet'][0]
        coldRisk = life_index['coldRisk'][0]
        comfort = life_index['comfort'][0]
        date = weather['result']['daily']['astro'][0]['date'][:10]

        citydraft = self.city+'今天'
        dateDraft = date + '。'
        temperatureDraft = '温度：' + \
            f"{temperature['max']} ~ {temperature['min']}" + '℃。 '
        windspeedDraft = '风力：' + \
            f"{wind['min']['speed']} ~ {wind['max']['speed']}" + 'm/s。 '
        winddrectionDraft = '风向：' + \
            Data.get_wind_direction(wind['avg']['direction'])
        precipitationDraft = '降水可能性：' + \
            f"{precipitation['probability']}" + '%。 '
        skyconDraft = '天气' + Data.WEATHER_DICT[skycon['value']] + '。'
        pm25Draft = '今天PM2.5: ' + \
            f"{air_quality['pm25'][0]['avg']}" + 'μg/m³。 '
        ultravioletDraft = '紫外线' + f"{ultraviolet['desc']}" + '，'
        coldRiskDraft = '感冒指数：' + f"{coldRisk['desc']}" + '。'
        comfortDraft = '体感' + f"{comfort['desc']}" + '，'

        draft = dateDraft + citydraft + skyconDraft + precipitationDraft + temperatureDraft + winddrectionDraft + \
            windspeedDraft + pm25Draft + ultravioletDraft + comfortDraft + coldRiskDraft

        self.result_str = draft


if __name__ == '__main__':
    a = GetWeather('北京')
    a.process_url()
    a.get_weather()
    a.pross_weather()
    print(a.result_str)
