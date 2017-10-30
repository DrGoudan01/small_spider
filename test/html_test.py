#__author__ = 'li'
# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
res = requests.get('https://www.shiyanlou.com/courses/')
soup = BeautifulSoup(res.text,'lxml')
#将请求到的页面利用lxml解析并保存
course = soup.find_all('div',{'class':'col-md-4','class':'col-sm-6','class':'course'})
#定义查找的div标签，这个方法是BeautifulSoup定义的
#遍历这个经过解析又经过筛选的列表
for i in course:
    title = i.find('div',{'class':'course-name'})