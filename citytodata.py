import csv


class CitytoData(object):
    def __init__(self, city):
        self.city = city
        self.location = ''

    def get_data(self):
        with open('city_data.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if self.city in row:
                    self.location = ''+str(row[5])+','+str(row[4])
                    print(self.location)
                    return self.location
            if len(self.location) == 0:
                print('没有找到该城市,请重新输入！示例：天津南开区->南开')
                return False


if __name__ == '__main__':
    city = CitytoData('北京')
    data = city.get_data()
    cata = CitytoData('北京').get_data()
    print(cata)
