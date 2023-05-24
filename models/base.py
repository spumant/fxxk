# -*- coding:utf-8 -*-
"""
@Des: 基础模型
"""

from tortoise import fields
from tortoise.models import Model
import mongoengine


class User(Model):
    privilege = fields.CharField(max_length=255, null=True, description='权限', )
    pwd = fields.CharField(max_length=255, null=True, description='密码', )
    uid = fields.IntField(pk=True, description='userid', )
    user_name = fields.CharField(max_length=255, null=True, description='名字', )
    view = fields.IntField(description='区分用户视图', )


class Worker(Model):
    age = fields.IntField(description='年龄', )
    e_mail = fields.CharField(max_length=255, null=True, description='邮件', )
    edu_level = fields.IntField(description='教育水平（最高）', )
    edu_school = fields.CharField(max_length=255, null=True, description='毕业院校（最高）', )
    location = fields.CharField(max_length=255, null=True, description='地点', )
    phone_number = fields.CharField(max_length=255, null=True, description='电话号码', )
    sex = fields.CharField(max_length=255, null=True, description='性别', )
    statue = fields.CharField(max_length=255, null=True, description='政治身份', )
    url_format = fields.CharField(max_length=255, null=True, description='简历文件格式标识', )
    urls = fields.CharField(max_length=255, null=True, description='简历url', )
    view = fields.IntField(description='区分用户视图', )
    wid = fields.IntField(pk=True, description='workerid', )
    work_year = fields.IntField(description='工作经历', )
    worker_name = fields.CharField(max_length=255, description='名字', )


class Worke_Match(Model):
    wid = fields.IntField(pk=True, description='workerid', )
    wm_1 = fields.FloatField(description='岗位1', )
    wm_2 = fields.FloatField(description='岗位2', )
    wm_3 = fields.FloatField(description='岗位3', )
    wm_4 = fields.FloatField(description='岗位4', )
    wm_5 = fields.FloatField(description='岗位5', )


class Item(mongoengine.Document):
    id = mongoengine.StringField()
    title = mongoengine.StringField()
    txt = mongoengine.ListField()
    img = mongoengine.StringField()
    tag = mongoengine.StringField()
    like = mongoengine.IntField()
    collection = mongoengine.IntField()
    meta = {'collection': 'item', 'strict': False}
