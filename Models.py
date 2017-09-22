#! /usr/bin/python3
# coding: utf-8

# 1. 导入peewee的模块
from peewee import MySQLDatabase,Model
from playhouse.pool import PooledMySQLDatabase
from peewee import *
import datetime
# 2. 建立数据库实例
db = PooledMySQLDatabase(
    database='test',
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    charset='utf8')

#######################################################################
# 3. 建立数据表的模型
# 4. 先建立基本模型，具体的模型在此基础上继承而来
class BaseModel(Model):
    class Meta:
        # 指定表所在的数据库
        database = db

class TrainSearch(BaseModel):
    id = PrimaryKeyField()
    trainNo = CharField()
    date = CharField()
    startStation = CharField()
    endStation = CharField()

