# -*- coding:utf-8 -*-
"""
@Des: schemas模型
"""
from datetime import datetime
from pydantic import Field, BaseModel
from typing import Optional, List


class UserInfo(BaseModel):
    id: int
    ids: List
