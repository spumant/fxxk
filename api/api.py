# -*- coding:utf-8 -*-
"""
@Des: api路由
"""
from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")
# api_router.include_router(user.router, prefix='/admin', tags=["用户管理"])
# api_router.include_router(access.router, prefix='/admin', tags=["权限管理"])
