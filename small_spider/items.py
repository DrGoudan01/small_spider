# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MovieSpiderItem(scrapy.Item):
    # 下面定义四个的原因是：该项目开始时，爬取目标就是标题、图片、描述和下载链接
    name = scrapy.Field()#固定代码，定义name
    pic = scrapy.Field()#固定代码，定义pic
    content = scrapy.Field()#固定代码，定义content
    download = scrapy.Field()#固定代码，定义download