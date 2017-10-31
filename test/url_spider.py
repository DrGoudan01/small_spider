#__author__ = 'li'
# -*- coding:utf-8 -*-
#这个函数的主要目的是获取所有页面的rurl
import requests
import re
from bs4 import BeautifulSoup
def main():
    res = requests.get('https://www.shiyanlou.com/courses/')
    soup = BeautifulSoup.find_all(res.text,'lxml')
    course_link = "https://www.shiyanlou.com/courses/?course_type=all&tag=all&fee=all&page={}"
    #这里定义了需要的链接的格式，这个格式在f12可以查看
    pape = soup.find_all('ul',{'class':'pagination'})
    #注意这里的ul标签，ul是一个无序的html列表，里面使用li的子标签
    if len(pape)<1 :
        print("it is false")
        return None
    li_num = pape[0].find_all('li')
    #print(li_num)
    #接下来只需要遍历和取最大值就可以了
    for i in li_num:
        try:
            li_num = int(i.find('a').get_text())#获取放在a标签的字符串数字，并用int强制转换
        except:
            li_num = 0#如果获取失败，则赋值0
        if li_num > page_num:#page_num永远保存最大的值
            page_num = li_num
    # print(page_num,type(page_num))
    for i in range(1,page_num+1):#拿到page_num数字，从1开始数到page_num
        print(course_link.format(i))#打印课程页的全部链接
if __name__ == "__main__":
    main()