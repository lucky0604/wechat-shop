# -*- coding: utf-8 -*-
"""
@Time    : 3/16/21 1:23 PM
@Author  : Lucky
@Email   : lucky_soft@163.com
@File    : middlewares.py
@Desc    : Description about this file
"""

class IPProxyMiddleware(object):

    def fetch_proxy(self):
        # You need to rewrite this function if you want to add proxy pool
        # the function should return a ip in the format of "ip:port" like "12.34.1.4:9090"
        return None

    def process_request(self, request, spider):
        proxy_data = self.fetch_proxy()
        if proxy_data:
            current_proxy = f'http://{proxy_data}'
            spider.logger.debug(f"current proxy:{current_proxy}")
            request.meta['proxy'] = current_proxy

