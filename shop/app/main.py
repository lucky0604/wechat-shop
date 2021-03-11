# -*- coding: utf-8 -*-
"""
@Time    : 3/11/21 12:36 PM
@Author  : Lucky
@Email   : lucky_soft@163.com
@File    : main.py
@Desc    : Description about this file
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1")
async def root():
    return {"message": "Hello Tiffany"}