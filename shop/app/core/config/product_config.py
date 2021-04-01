# -*- coding: utf-8 -*-
"""
@Time    : 4/1/21 3:23 PM
@Author  : Lucky
@Email   : lucky_soft@163.com
@File    : product_config.py
@Desc    : Description about this file
"""
import os
from typing import List, Union
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress, EmailStr

class Settings(BaseSettings):
    DEBUG: bool = True
    API_V1_STR: str = "/api/shop/v1"
    SECRET_KEY: str = "(-ASp+_)-Ulhw0848hnvVG-iqKyJSD&*&^-H3C9mqEqSl8KN-YRzRE"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # project info
    PROJECT_NAME: str = "Wechat Shop"
    DESCRIPTION: str = "Wechat shop"
    SERVER_NAME: str = "API_V1"
    SERVER_HOST: AnyHttpUrl = "http://127.0.0.1:8020"
    BACKEND_CORS_ORIGINS: List[str] = ['*']

    # mysql config

    MYSQL_USERNAME: str = "root"
    MYSQL_PASSWORD: str = "1234"
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "127.0.0.1"
    MYSQL_DATABASE: str = 'wechat_shop'
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"

    # redis config
    REDIS_HOST: str = "127.0.0.1"
    REDIS_PASSWORD: str = ""
    REDIS_DB: int = 0
    REDIS_PORT: int = 6379
    REDIS_URL: str = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}?encoding=utf8"

    # basic role permission
    DEFAULT_ROLE: List[dict] = [
        {"role_id": 100, "role_name": "普通用户", "permission_id": 100},
        {"role_id": 500, "role_name": "商户", "permission_id": 500},
        {"role_id": 999, "role_name": "管理员", "permission_id": 999}
    ]

    # default user
    FIRST_SUPERUSER: str = "admin"
    FIRST_MALL: EmailStr = "admin@weshop.com"
    FIRST_SUPERUSER_PASSWORD:str = "123456"
    FIRST_ROLE: int = 999
    FIRST_AVATAR: AnyHttpUrl = ""

    class Config:
        case_sensitive = True

settings = Settings()