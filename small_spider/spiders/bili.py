#__author__ = 'li'
# -*- coding:utf-8 -*-
#文件名:comedy.py
import scrapy
import re
import urllib
from ..items import MovieSpiderItem
class movie87_spider(scrapy.Spider):
name = "comedy"#定义爬虫名字
allowed_domains = ["www.87movie.com"]#允许的域名
start_urls = ["http://www.87movie.com/tag/%E5%96%9C%E5%89%A7/"]
def parse(self,response):
    num_page = response.xpath('//ul[@class="pagination"]//li[last()]/a/@herf]').extract()
    number = 1
    if len(num_page)>0:
        number = int(num_page[0].split('/')[-1].split('?')[0])
        for i in range(1,number+1):
            yield scrapy.Request(response.url+str(i)+'?o=data',callback=self.prase_page)
            #注意此处函数的调用方法，在scrapy中除了parse函数其他都不可以直接调用response参数，必须使用这种方法调用二级函数
            #语法是scrapy.Request(url, callback=self.函数名)
def parse_page(self, response):
    movies = response.xpath('//ul[@class="list-unstyled mlist"]/li//h4/a/@href').extract()
    url_host = 'http://' + response.url.split('/')[2]
    for i in movies:
        movie_info = MovieSpiderItem()
        yield scrapy.Request(url_host+i, meta={'movie_info': movie_info, 'demo':'demo demo demo demo demo demo'},\
                                 callback=self.parse_info) # , 'demo':'demo demo demo demo demo demo' 为演示代码
def parse_info(self, response):
    movie_info = response.meta['movie_info']
    demo = response.meta['demo'] # 演示代码
    print(demo) # 演示代码