import requests
from requests.exceptions import RequestException
from fake_useragent import UserAgent
headers = {"User-Agent": UserAgent().firefox}
url = 'https://tophub.today'


def get_page(url)->str:
        try:
            response = requests.get(url,headers=headers)
            if response.status_code == 200:
                with open('News.html','w',encoding='utf-8') as f:
                    f.write(response.text)
                print(response.text)
                return response.text
        except RequestException as e:
            return None
        

print(get_page(url))
