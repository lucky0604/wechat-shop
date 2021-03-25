# -*- coding: utf-8 -*-
"""
@Time    : 3/16/21 1:14 PM
@Author  : Lucky
@Email   : lucky_soft@163.com
@File    : run_spider.py
@Desc    : Description about this file
"""
import os
import sys
from spiders.shop import ShopSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    mode = sys.argv[1]
    os.environ['SCRAPY_SETTINGS_MODULE'] = f'settings'
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    mode_to_spider = {
        'shop': ShopSpider
    }
    print(mode_to_spider[mode], ' ------ start spider --------')
    process.crawl(mode_to_spider[mode])
    process.start()