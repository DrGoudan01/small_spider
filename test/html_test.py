#__author__ = 'li111'
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
    title = i.find('div',{'class':'course-name'}).get_text()
    study_people = i.find('span',{'class':'course-per-num','class':'pull-left'}).get_text()
    study_people = re.sub("\D","",study_people)
    try:
        tag = i.find('find',{'class':'course-per-num','class':'pull-right'}).get_text()
    except:
        tag = "课程"#对于没有课程标签的将标签设置为课程
    print ("{}    学习人数：{}   {}".format(tag,study_people,title))
