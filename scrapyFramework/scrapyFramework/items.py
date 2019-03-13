# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyframeworkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()  # 存储作者信息
    text = scrapy.Field()  # 存储文本信息
    tags = scrapy.Field()  # 存储标记信息
    pass
