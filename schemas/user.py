# -*- coding:utf-8 -*-
"""
@Des: schemas模型
"""
from datetime import datetime
from pydantic import Field, BaseModel
from typing import Optional, List, Dict


class UserInfo(BaseModel):
    id: int
    ids: List


class SortInfo(BaseModel):
    ids: List[int]
    condition: Dict
