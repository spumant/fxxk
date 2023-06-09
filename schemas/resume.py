from pydantic import BaseModel
from typing import List, Optional


class ItemCheck(BaseModel):
    id: int  # 用户id
    skills: List  # 技能列表
    jobHunt: str  # 求职意愿
    self: str  # 自我评价
    # experiences: str  # 工作经历
    # educational: str  # 教育经历
    award: List  # 获奖证书
    letter: Optional[str]  # 自荐书
