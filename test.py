a = {'status': 'ok', 'api_version': 'v2.6', 'api_status': 'alpha', 'lang': 'zh_CN', 'unit': 'metric', 'tzshift': 28800, 'timezone': 'Asia/Shanghai', 'server_time': 1671973477, 'location': [35.58066, 104.6106], 'result': {'alert': {'status': 'ok', 'content': [], 'adcodes': [{'adcode': 620000, 'name': '甘肃省'}, {'adcode': 621100, 'name': '定西市'}, {'adcode': 621102, 'name': '安定区'}]}, 'daily': {'status': 'ok', 'astro': [{'date': '2022-12-25T00:00+08:00', 'sunrise': {'time': '08:08'}, 'sunset': {'time': '17:54'}}], 'precipitation_08h_20h': [{'date': '2022-12-25T00:00+08:00', 'max': 0.0715, 'min': 0.0, 'avg': 0.0106, 'probability': 0}], 'precipitation_20h_32h': [{'date': '2022-12-25T00:00+08:00', 'max': 0.0, 'min': 0.0, 'avg': 0.0, 'probability': 0}], 'precipitation': [{'date': '2022-12-25T00:00+08:00', 'max': 0.0715, 'min': 0.0, 'avg': 0.0, 'probability': 0}], 'temperature': [{'date': '2022-12-25T00:00+08:00', 'max': -3.0, 'min': -16.0, 'avg': -7.9}], 'temperature_08h_20h': [{'date': '2022-12-25T00:00+08:00', 'max': -3.0, 'min': -16.0, 'avg': -6.69}], 'temperature_20h_32h': [{'date': '2022-12-25T00:00+08:00', 'max': -4.33, 'min': -15.9, 'avg': -11.39}], 'wind': [{'date': '2022-12-25T00:00+08:00', 'max': {'speed': 23.32, 'direction': 353.25}, 'min': {'speed': 0.28, 'direction': 129.13}, 'avg': {'speed': 9.4, 'direction': 344.25}}], 'wind_08h_20h': [{'date': '2022-12-25T00:00+08:00', 'max': {'speed': 14.31, 'direction': 330.47}, 'min': {'speed': 0.28, 'direction': 129.13}, 'avg': {'speed': 8.32, 'direction': 336.79}}], 'wind_20h_32h': [{'date': '2022-12-25T00:00+08:00', 'max': {'speed': 8.25, 'direction': 166.63}, 'min': {'speed': 3.3, 'direction': 84.32}, 'avg': {'speed': 5.32, 'direction': 163.31}}], 'humidity': [{'date': '2022-12-25T00:00+08:00', 'max': 0.68, 'min': 0.29, 'avg': 0.37}], 'cloudrate': [{'date': '2022-12-25T00:00+08:00', 'max': 1.0, 'min': 0.3, 'avg': 0.46}], 'pressure': [{'date': '2022-12-25T00:00+08:00', 'max': 79851.3, 'min': 79594.55, 'avg': 79681.25}], 'visibility': [{'date': '2022-12-25T00:00+08:00', 'max': 24.13, 'min': 9.34, 'avg': 16.48}], 'dswrf': [{'date': '2022-12-25T00:00+08:00', 'max': 255.2, 'min': 0.0, 'avg': 0.0}], 'air_quality': {'aqi': [{'date': '2022-12-25T00:00+08:00', 'max': {'chn': 111, 'usa': 119}, 'avg': {'chn': 56, 'usa': 112}, 'min': {'chn': 38, 'usa': 54}}], 'pm25': [{'date': '2022-12-25T00:00+08:00', 'max': 43, 'avg': 40, 'min': 14}]}, 'skycon': [{'date': '2022-12-25T00:00+08:00', 'value': 'PARTLY_CLOUDY_NIGHT'}], 'skycon_08h_20h': [{'date': '2022-12-25T00:00+08:00', 'value': 'CLOUDY'}], 'skycon_20h_32h': [{'date': '2022-12-25T00:00+08:00', 'value': 'PARTLY_CLOUDY_NIGHT'}], 'life_index': {'ultraviolet': [{'date': '2022-12-25T00:00+08:00', 'index': '1', 'desc': '最弱'}], 'carWashing': [{'date': '2022-12-25T00:00+08:00', 'index': '1', 'desc': '适宜'}], 'dressing': [{'date': '2022-12-25T00:00+08:00', 'index': '8', 'desc': '极冷'}], 'comfort': [{'date': '2022-12-25T00:00+08:00', 'index': '12', 'desc': '湿冷'}], 'coldRisk': [{'date': '2022-12-25T00:00+08:00', 'index': '4', 'desc': '极易发'}]}}, 'primary': 0}}
print(a['result']['daily'].keys())
print(a['result']['daily']['life_index'].keys())

temperature = a['result']['daily']['temperature'][0]
wind = a['result']['daily']['wind'][0]
air_quality = a['result']['daily']['air_quality']
skycon = a['result']['daily']['skycon'][0]
temperatureDraft = '今日温度：' +f"{temperature['max']} ~ {temperature['min']}"  + '℃~'
precipitation = a['result']['daily']['precipitation'][0]
life_index = a['result']['daily']['life_index']
ultraviolet = life_index['ultraviolet'][0]
dressing = life_index['dressing'][0]
coldRisk= life_index['coldRisk'][0]
comfort = life_index['comfort'][0]



# print(life_index['desc'])
print(ultraviolet['desc'])

import re

date = {'date':"2022-12-27T00:00+08:00"}
print(date['date'][:10])
print(a['result']['daily']['astro'][0]['date'][:10])
print