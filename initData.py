#!/usr/bin/python3
# -*- coding:utf-8 -*-
import urllib3
import json
import pymysql
from common import *
urllib3.disable_warnings()


'''

初始化车站

'''
stationlist_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9026'  

resp = http.request('GET', stationlist_url,headers=hd)

stationlist = resp.data.decode('utf-8').split('@')
lineNo=0
with open('./ST.txt', 'w',encoding = 'utf-8') as f:
    for stationInfo in stationlist:
        if lineNo !=0:
            f.write(stationInfo.replace("';",""))
            f.write('\n')
        lineNo=lineNo+1
