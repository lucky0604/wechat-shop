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
from lxml import etree
from chardet import detect

class ShopSpider(scrapy.Spider):
    name = "shop_spider"
    start_urls = [
        'http://www.bao66.cn/web/',
    ]

    def parse(self, response):
        # myparser = etree.HTMLParser(encoding="utf-8")
        # tree_node = etree.HTML(response.body, parser=myparser)
        # good_list = tree_node.xpath('//li[@class="f-product"]')
        # print(good_list, ' ------ print body ----')
        # for item in good_list:
        #     shop_item = IndexItem()
        #     shop_item["item_desc"] = item.xpath('.//img/@src')
        #     yield shop_item
        li_list = response.xpath('//li[@class="inline-block f-product"]')
        print(li_list, ' ---- li list -------')
        for item in li_list:
            print(item, ' ----- item ------')
            shop_item = IndexItem()
            # shop_item["item_desc"] = item.css('img.').get()
            print(item.xpath('.//p[@class="product_desc"]/text()'), ' ---- item desc ------')
            shop_item["item_desc"] = item.xpath('.//p[@class="product_desc"]/text()').extract()[0]

            yield shop_item
