# -*- coding: utf-8 -*-
"""
@Time    : 3/23/21 1:27 PM
@Author  : Lucky
@Email   : lucky_soft@163.com
@File    : item.py
@Desc    : Description about this file
"""
from scrapy import Item, Field

class IndexItem(Item):
    _id = Field()
    item_avatar = Field()
    item_desc = Field()
    item_title = Field()
    item_price = Field()
