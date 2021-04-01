# -*- coding: utf-8 -*-
"""
@Time    : 4/1/21 2:50 PM
@Author  : Lucky
@Email   : lucky_soft@163.com
@File    : __init__.py.py
@Desc    : Description about this file
"""
import os
env = os.getenv("ENV", "")
if env:
    from .product_config import settings
else:
    from .development_config import settings