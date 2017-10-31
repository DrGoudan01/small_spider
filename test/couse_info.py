#__author__ = 'li'
# -*- coding:utf-8 -*-
#这个函数主要是对具体的课程页面进行信息的获取
import requests
from bs4 import BeautifulSoup
import time
def write_file(string):
    log = open('/home/shiyanlou/Desktop/shiyanlou_spider.log','a')#打开文件，a是参数
    log.write(string+'\n')#写进去，记得换行，不然全部粘结在一起
    log.close()#关闭
url="xx"
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
print(soup)
type_list = soup.select('ol[class=bareadcrumb]>li>a')
#此处调用了新的的查找select方式，这个查找方式可以递归查询，查找ol且class=b的标签下li的a
types = []
for i in type_list:
    if type_list.index(i)!=0 and type_list.index(i)!=len(type_list)-1:
        #除去头元素和尾元素，这个index函数是用于查找列表中元素的位置
        types.append(i.get_text())
#获取课程信息
info = soup.find('div',{'class':'course-infobox-content'})
info = info.find('p').get_text()
name = soup.find('div',{'class':'name'})#查询课程名的html
name = name.find('strong').get_text()#获取课程名的字符串
#获取课程列表，较为复杂
labs = soup.find('div',{'id':'labs'})#查询标签
test_list = labs.find_all('div',{'class':'lab-item'})#可能有多个，用find_all函数
tests_name = []#预先定义列表
for i in test_list:#for循环，将标签全部获取出来并追加到列表中
    name = i.find('div',{'class':'lab-item-title'}).get_text()
    tests_name.append(name)
print("{}  {}  {}  {}".format(name,info,'&'.join(types)))
#注意此处的join是插入&作为间隔符使一个列表变为一个整体
#写入log文件，使用*作为间隔
for i in tests_name:
    write_file(i)
write_file('*'*100)
#每次抓取睡眠0.5s
time.sleep(0.5)

#加入一个日志记录文件
