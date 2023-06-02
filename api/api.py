# -*- coding:utf-8 -*-
"""
@Des: api路由
"""
from fastapi import APIRouter
from api.endpoints import exp
from api.endpoints import classification
from api.endpoints import similar

api_router = APIRouter(prefix="/api/v1")
# api_router.include_router(user.router, prefix='/admin', tags=["用户管理"])
# api_router.include_router(access.router, prefix='/admin', tags=["权限管理"])
api_router.include_router(exp.router, tags=['提取工作年限'])
api_router.include_router(classification.router, tags=['职位匹配与人才画像'])
api_router.include_router(similar.router, tags=['文本相似度'])
