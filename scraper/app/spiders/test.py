# -*- coding: utf-8 -*-
"""
@Time    : 3/16/21 1:28 PM
@Author  : Lucky
@Email   : lucky_soft@163.com
@File    : test.py
@Desc    : Description about this file
"""
import scrapy

class ShopSpider(scrapy.Spider):
    name = "shop_spider"
    base_url = "https://www.zyte.com/blog/"

    def parse(self, response):
        for title in response.css('.oxy-post-title'):
            yield {'title': title.css('::text').get()}
