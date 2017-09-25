#!/usr/bin/python3
# -*- coding:utf-8 -*-
import urllib3
import json
import pymysql
from common import *
import pandas as pd

station=pd.read_csv('ST.txt',sep='|',header=None,encoding='utf-8')
station.columns = ['pyshort', 'name', 'code', 'pylong', 'e','id']

def getUrl(train_no, from_station_telecode, to_station_telecode,depart_date):
 # 'https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no=580000T3060C&from_station_telecode=FZS&to_station_telecode=BJY&depart_date=2017-10-01'   
    urlTpl = 'https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no=%s&from_station_telecode=%s&to_station_telecode=%s&depart_date=%s'
    url = urlTpl % (train_no, from_station_telecode, to_station_telecode,depart_date)
    return url

def trainNo_station(train_no, from_station_telecode, to_station_telecode,depart_date):
    url=getUrl(train_no, from_station_telecode, to_station_telecode,depart_date)
    resp = http.request('GET', url,headers=hd)
    data = json.loads(resp.data.decode('utf-8'))
    trains = data['data']['data']
    return trains

def trainNo_station_code(train_no, from_station_telecode, to_station_telecode,depart_date):
    trainCode=[]
    trains=trainNo_station(train_no, from_station_telecode, to_station_telecode,depart_date)
    for t in trains:
        trainCode.append(t['station_name'])
    nostation=pd.DataFrame(trainCode,columns=['zh'])
    out=pd.merge(nostation, station, left_on='zh',right_on='name')
    return out.code









