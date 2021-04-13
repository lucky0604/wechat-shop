# -*- coding: utf-8 -*-
"""
@Time    : 4/2/21 1:28 PM
@Author  : Lucky
@Email   : lucky_soft@163.com
@File    : logger.py
@Desc    : Description about this file
"""
import os
import timer
from loguru import logger
from core.config import settings

# 定位到日志文件
log_path = os.path.join(settings.BASE_DIR, "logs")

if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path_error = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_error.log')

logger.add(log_path_error, rotation = "12:00", retention = "5 days", enqueue = True)

__all__ = ["logger"]