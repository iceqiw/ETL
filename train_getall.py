#!/usr/bin/python3
# -*- coding:utf-8 -*-
import urllib3
import json
import pymysql
from common import *
from trains_num import *

import time
#返回当前时间
def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def getUrl(date, start, end):
    urlTpl = 'http://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'
    url = urlTpl % (date, start, end)
    return url


def requestData(date, start, end, trainNo, isfirst=True):
    url = getUrl(date, start, end)
    # print(url)
    resp = http.request('GET', url, headers=hd)
    parseData(resp, start, date, trainNo, isfirst)


def parseData(resp, start, date, trainNo, isfirst):
    data = json.loads(resp.data.decode('utf-8'))
    trains = data['data']['result']
    stations = data['data']['map']
    for train in trains:
        trainInfo = parseTrain(train)
        if trainNo == trainInfo['train']:
            if isfirst:
                listStation = trainNo_station_code(trainInfo['trainCode'],
                                                   trainInfo['start'],
                                                   trainInfo['end'], date)
                for s in listStation:
                    if s!=start:
                        try:
                            requestData(date, start, s, trainNo, False)
                        except Exception as ex:
                            print(ex)
            trainInfo['start'] = stations[trainInfo['start']]
            trainInfo['end'] = stations[trainInfo['end']]
            trainInfo['modifyTime']= GetNowTime()
            print(trainInfo)
                        


def parseTrain(train):
    line = train.split('|')
    res = {}
    res['trainCode'] = line[2]
    res['train'] = line[3]
    res['date'] = line[13]
    res['start'] = line[6]  #起点
    res['end'] = line[7]  #终点
    res['rw'] = line[23]  #软卧
    res['yw'] = line[28]  #硬卧
    res['yz'] = line[29]  #硬座
    res['wz'] = line[26]  #无座

    return res

requestData('2017-10-01', 'FZS', 'BJY', 'T306')
