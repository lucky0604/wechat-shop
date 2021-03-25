# -*- coding: utf-8 -*-
"""
@Time    : 3/16/21 1:28 PM
@Author  : Lucky
@Email   : lucky_soft@163.com
@File    : shop.py
@Desc    : Description about this file
"""
import scrapy
from items import IndexItem
from scrapy_redis.spiders import RedisSpider

class ShopSpider(scrapy.Spider):
    name = "shop_spider"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            shop_item = IndexItem()
            shop_item["item_desc"] = quote.css('span.text::text').get()
            yield shop_item

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)