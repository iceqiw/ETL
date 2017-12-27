#!/usr/bin/python3
# -*- coding:utf-8 -*-
import urllib3
import json
from common import *
from Models import train_search
import time
from Email import *
#返回当前时间
def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def getUrl(date, start, end):
    urlTpl = 'http://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'
    url = urlTpl % (date, start, end)
    return url


def requestData(date, start, end, trainNo, isfirst=True):
    url = getUrl(date, start, end)
    print(url)
    resp = http.request('GET', url, headers=hd)
    parseData(resp, start, date, trainNo, isfirst)


def parseData(resp, start, date, trainNo, isfirst):
    data = json.loads(resp.data.decode('utf-8'))
    trains = data['data']['result']
    stations = data['data']['map']
    for train in trains:
        trainInfo = parseTrain(train)
        print(trainInfo)
        runSend(trainInfo)
       
                        
def parseTrain(train):
    line = train.split('|')
    res = {}
    res['trainCode'] = line[2]
    res['train'] = line[3]
    res['date'] = line[13]
    res['start'] = line[6]  #起点
    res['end'] = line[7]  #终点
    res['soft_sleeper'] = line[23]  #软卧
    res['hard_sleeper'] = line[28]  #硬卧
    res['hard_seat'] = line[29]  #硬座
    res['none_seat'] = line[26]  #无座
    return res

if __name__=="__main__":
    while True:
        for t in train_search.select():
            requestData(t.date, t.start_station, t.end_station, t.train_no)
