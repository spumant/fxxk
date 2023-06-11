# -*- coding:utf-8 -*-
"""
@Des: 基础模型
"""

from tortoise import fields
from tortoise.models import Model


class User(Model):
    uid = fields.IntField(pk=True, )
    hash_code = fields.CharField(unique=True, max_length=255, null=True, )


class Worker(Model):
    wid = fields.IntField(pk=True, )
    worker_name = fields.CharField(index=True, max_length=255, )
    sex = fields.CharField(max_length=255, null=True, )
    age = fields.CharField(max_length=255, null=True, )
    phone_number = fields.CharField(max_length=255, null=True, )
    e_mail = fields.CharField(max_length=255, null=True, )
    location = fields.CharField(max_length=255, null=True, )
    edu_school = fields.CharField(max_length=255, null=True, )
    edu_level = fields.CharField(max_length=255, null=True, )
    work_year = fields.IntField()
    statue = fields.CharField(max_length=255, null=True, )
    urls = fields.CharField(max_length=255, null=True, )
    url_format = fields.CharField(max_length=255, null=True, )
    hash_code = fields.CharField(unique=True, max_length=255, null=True, )


class Matchwork(Model):
    minfo = fields.IntField(pk=True, )
    wid = fields.IntField(index=True, )
    jid = fields.IntField()
    match = fields.FloatField()


class Job(Model):
    jid = fields.IntField(pk=True, )
    jname = fields.CharField(index=True, max_length=255, null=True, )
    jneed_age = fields.IntField()
    jneed_edu = fields.CharField(max_length=255, null=True, )
    jneed_other = fields.TextField(null=True, )
    jneed_year = fields.CharField(max_length=255, null=True, )
    hash_code = fields.CharField(index=True, max_length=255, null=True, )


class Have(Model):
    hid = fields.IntField(pk=True, )
    uid = fields.IntField(index=True, )
    wid = fields.IntField()
