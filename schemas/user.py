# -*- coding:utf-8 -*-
"""
@Des: schemas模型
"""
from datetime import datetime
from pydantic import Field, BaseModel
from typing import Optional, List


class UserInfo(BaseModel):
    uid: int
    view: int
    username: str
    pwd: str
    privilege: str


class WorkeMatchInfo(BaseModel):
    wid: int
    wm1: float
    wm2: float
    wm3: float
    wm4: float
    wm5: float


class WorkerInfo(BaseModel):
    wid: int
    view: int
    worker_name: str
    sex: str
    age: int
    phone_number: str
    email: str
    location: str
    edu_school: str
    edu_level: int
    work_year: int
    statue: str
    urls: str
    url_format: str


class Item(BaseModel):
    id: int

