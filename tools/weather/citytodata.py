#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: citytodata.py


import csv
from tools.error import CsvParserError


class CitytoData(object):
    '''
    从csv文件获取对应城市的数据

    例如：

    cata = CitytoData('北京').get_data()

    如果出错会引起异常: CsvParserError
    '''

    def __init__(self, city):
        self.city = city
        self.location = ''

    def get_data(self):
        csv_path = './assets/weatherdata/city_data.csv'
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if self.city in row:
                        self.location = ''+str(row[5])+','+str(row[4])
                        print(self.location)
                        return self.location
                if len(self.location) == 0:
                    print('没有找到该城市,请重新输入！示例：天津南开区->南开')
                    return False
        except Exception as e:
            raise CsvParserError(f'无法解析csv文件，error: {e}')


if __name__ == '__main__':
    city = CitytoData('北京')
    data = city.get_data()
    cata = CitytoData('北京').get_data()
    print(cata)
