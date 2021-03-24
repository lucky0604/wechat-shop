# -*- coding: utf-8 -*-
"""
@Time    : 3/16/21 1:24 PM
@Author  : Lucky
@Email   : lucky_soft@163.com
@File    : pipelines.py
@Desc    : Description about this file
"""
import pymongo
from pymongo.errors import DuplicateKeyError
from items import IndexItem
from settings import MONGO_HOST, MONGO_PORT

class MongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        db = client["shop"]
        self.ShopItems = db["Shop"]

    def process_item(self, item, spider):
        if spider.name == "shop":
            self.insert_item(self.ShopItems, item)
        return item

    @staticmethod
    def insert_item(collection, item):
        try:
            collection.insert(dict(item))
        except DuplicateKeyError:
            pass