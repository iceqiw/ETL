#!/usr/bin/python3
# -*- coding:utf-8 -*-
import urllib3
import json
import time
import argparse
import smtplib
import email.mime.multipart  
import email.mime.text

urllib3.disable_warnings()

FLAGS={}

parser = argparse.ArgumentParser()
# Basic model parameters.
parser.add_argument(
    '--start_station',
    type=str,
    default='FZS',
    help='train start_station')

parser.add_argument(
    '--end_station',
    type=str,
    default='BJY',
    help='train end_station')

parser.add_argument(
    '--train_no',
    type=str,
    default='T306',
    help=' train_no')

parser.add_argument(
    '--date',
    type=str,
    default='2018-01-26',
    help='train date .')

parser.add_argument(
    '--query_key',
    type=str,
    default='query',
    help='querykey .')

parser.add_argument(
    '--password',
    type=str,
    default='qupasswordery',
    help='password .')

hd = {
    'user-agent':
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
    'accept':
    "*/*",
    'cache-control':
    "no-cache",
    'referer':
    "https://kyfw.12306.cn/otn/leftTicket/init",
    'accept-encoding':
    "gzip, deflate, br",
    'accept-language':
    "zh-CN,zh;q=0.8,en;q=0.6",
    'cookie':
    "JSESSIONID=5CABAA927C870655B853A255CFFDB1E3; tk=pNogcAkbGN8AtUUqNaBv8vcFVlrefEfLwQSoSwijq1q0; RAIL_EXPIRATION=1514530584881; RAIL_DEVICEID=q5ztWh4ue0k2CNXwc3i060RfZf40DEPxMOgE4GRB2uDbGNE5xWF8XpBfpenAhUKLi3hykaggFuH9j7a0sLRub_6nWDABplZ0f3vWbwDPM8XfRHtvuY2KrXsTh-hFCsgAMiT0wO9eashzihlcjhWU6KrG9SpVTE2C; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=1977155850.50210.0000; BIGipServerpassport=786956554.50215.0000; current_captcha_type=Z; _jc_save_fromStation=%u798F%u5DDE%2CFZS; _jc_save_toStation=%u4E4C%u9C81%u6728%u9F50%2CWAR; _jc_save_fromDate=2018-01-25; _jc_save_toDate=2017-12-27; _jc_save_wfdc_flag=dc"
}

#返回当前时间
def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def getUrl(date, start, end,querykey):
    urlTpl = 'http://kyfw.12306.cn/otn/leftTicket/%s?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'
    url = urlTpl % (querykey,date, start, end)
    return url


def requestData(http,date, start, end, trainNo, querykey,isfirst=True):
    url = getUrl(date, start, end,querykey)
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
        sendEmail(trainInfo)
                          
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


def sendEmail(train):
    if train['hard_sleeper'] == '无':
        print('-----------------------raise-----------------------')
        return False
    if train['hard_sleeper'] == '*':
        print('-----------------------raise-----------------------')
        return False
    print('-----------------------sendEmail-----------------------')
    msg = email.mime.multipart.MIMEMultipart()  
    msg['Subject'] = "END:"+train['end']+",hard_sleeper:"+train['hard_sleeper']
    msg['From'] = 'qqwei1123@163.com'
    msg['To'] ='418419818@qq.com'  
    content = ''' 
        通知 train ticket
        end:%s
        hard_sleeper:%s 
        soft_sleeper:%s 
        date:%s 
        send
    '''
    content = content % (train['end'],train['hard_sleeper'],train['soft_sleeper'],train['date'])

    txt = email.mime.text.MIMEText(content)  
    msg.attach(txt)  
    smtp = smtplib.SMTP_SSL()
    smtp.connect('smtp.163.com',465)
    smtp.login('qqwei1123@163.com', FLAGS.password)
    smtp.sendmail('qqwei1123@163.com',['418419818@qq.com','54018875@qq.com'], msg.as_string())
    smtp.quit()
    print('-----------------------ok-----------------------')

if __name__=="__main__":
    http = urllib3.PoolManager(cert_reqs='CERT_NONE')
    FLAGS, unparsed = parser.parse_known_args()
    while True:
        try:
           requestData(http,FLAGS.date, FLAGS.start_station, FLAGS.end_station, FLAGS.train_no,FLAGS.query_key) 
        except Exception as ex:
            print(ex)
        time.sleep(5)
