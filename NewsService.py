#! /usr/bin/env python
# encoding=utf-8
# author: L.S.

import requests
from bottle import template
from lxml import etree
from requests.exceptions import RequestException
from fake_useragent import UserAgent
from os import remove, path
import logging
from EmailPushService import SendEmail, EmailInformation
from tools.weather.get_weather import GetWeather
from tools.weather.get_token import get_token

class NewsInfo(object):
    xpath_dict = {
        # 知乎
        'zhihu': ['知乎', '//div[@id="node-4439"]//div[@class="cc-cd-cb-l nano-content"]/a'],
        # 百度贴吧
        'bdtb': ['百度贴吧', '//div[@id="node-3"]//div[@class="cc-cd-cb-l nano-content"]/a'],
        # 第一财经
        'dycj': ['第一财经', '//div[@id="node-2413"]//div[@class="cc-cd-cb-l nano-content"]/a'],
        # 财新网
        'cxw': ['财新网', '//div[@id="node-2496"]//div[@class="cc-cd-cb-l nano-content"]/a'],
        # 新浪财经新闻
        'xlcjxw': ['新浪财经新闻', '//div[@id="node-252"]//div[@class="cc-cd-cb-l nano-content"]/a'],
        # 历史上的今天
        'lssdjt': ['历史上的今天', '//div[@id="node-369"]//div[@class="cc-cd-cb-l nano-content"]/a'],
        # 高楼迷
        'gaoloumi': ['高楼迷', '//div[@id="node-2954"]//div[@class="cc-cd-cb-l nano-content"]/a'],
        # 起点中文网
        'qdzww': ['起点中文网', '//div[@id="node-5832"]//div[@class="cc-cd-cb-l nano-content"]/a'],
        # 纵横中文网
        'zhzww': ['纵横中文网', '//div[@id="node-5846"]//div[@class="cc-cd-cb-l nano-content"]/a'],
        # 咖啡日报
        'kfrb': ['咖啡日报', '//div[@id="node-273"]//div[@class="cc-cd-cb-l nano-content"]/a'],
        # 开发者头条
        'kfztt': ['开发者头条', '//div[@id="node-132"]//div[@class="cc-cd-cb-l nano-content"]/a'],
        # IT之家
        'ITHome': ['IT之家', '//div[@id="node-119"]//div[@class="cc-cd-cb-l nano-content"]/a']
    }


class GetNews(object):

    def __init__(self) -> None:
        self.url = 'https://tophub.today'
        self.html = None
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, filemode='w', filename='Newslog.txt',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.headers = {"User-Agent": UserAgent().firefox}

        self.content = []
        self.test_file_path = 'News.html'
        self.news_content = {}

        self.logger.info('NewPush init Success!')

    def get_page(self) -> str:
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                self.html = response.text
                self.logger.info('Get News Page Success!')
                return self.html
        except RequestException as e:
            self.logger.error(e)
            return None

    def process_page(self):
        self.logger.info('Procedding News Page...')
        news_info = NewsInfo()
        html_text = self.html
        # 读取并解析html内容
        etree_html = etree.HTML(html_text)
        try:
            for key in news_info.xpath_dict:
                alist = etree_html.xpath(news_info.xpath_dict[key][1])
                for a in alist:
                    text = a.xpath('.//span[@class="t"]/text()')[0]
                    link = a.get('href')
                    temp = [text, link]
                    self.content.append(temp)

                self.news_content[news_info.xpath_dict[key][0]] = self.content
                self.content = []

            self.logger.info('Process News Page Success!')
            return self.news_content

        except Exception as e:
            self.logger.error(e)
            return None


    @staticmethod
    def generate_html_file(file_template_path, generated_file_path, weather_info, news_info):
        html = template(file_template_path,
                        weather_info=weather_info, info_dict=news_info)
        with open(generated_file_path, 'w', encoding='utf-8') as f:
            f.write(html)

    @staticmethod
    def remove_file(filename, logger):
        try:
            if path.exists(filename):
                remove(filename)
        except FileNotFoundError as e:
            logger.error(e)

    @staticmethod
    def save_source_info(filename, source_info):
        with open(filename, 'a+', encoding='utf-8') as f:
            f.write(source_info)

    @staticmethod
    def read_html_file(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()


if __name__ == '__main__':

    News = GetNews()
    News.get_page()
    news_info = News.process_page()
    
    a = GetWeather('北京', get_token('token.txt'))
    a.process_url()
    a.get_weather()
    weather_info = a.pross_weather()

    News.generate_html_file(
        'NewsTempelate.html', 'Newsgenerated.html', weather_info, news_info)

    info = {'sender': '1157723200@qq.com', 'token': 'mqrsefodflqejcji', 'receivers': ['1157723200@qq.com', 'azureqaq@icloud.com'], 'header': {
        'HeaderFrom': 'Personal Intelligence System', 'HeaderTo': 'BOSS'}, 'subject': 'Email test', 'message': 'This is a test email.'}
    with open('htmltest.html', 'r', encoding='utf-8') as f:
        send = f.read()
        info['message'] = send

    email_info = EmailInformation(**info)
    send = SendEmail(email_info)
    try:
        send.sever_login()
        send.send_email()
    except Exception as e:
        print(e)
        send.sever_logout()
    print(news_info)
