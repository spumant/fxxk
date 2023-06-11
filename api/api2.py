from fastapi import APIRouter
from api.endpoints import exp
from api.endpoints import classification
from api.endpoints import similar
from api.endpoints import all

api_router2 = APIRouter(prefix='/api/v2')
api_router2.include_router(all.router, tags=['整合api'])
