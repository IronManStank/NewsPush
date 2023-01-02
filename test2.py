# encoding: utf-8
from NewsService import GetNews
from bottle import SimpleTemplate, template

News = GetNews()

news_info = News.process_page()
        
html = template('NewsTempelate.html',info_dict=news_info)
with open('htmltest.html','w',encoding='utf-8') as f:
        f.write(html)

