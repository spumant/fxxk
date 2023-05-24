# -*- coding:utf-8 -*-
"""
@Des: 路由聚合
"""
from api.api import api_router
from fastapi import APIRouter


router = APIRouter()
# 视图路由
# router.include_router(views_router)
# API路由
router.include_router(api_router)

