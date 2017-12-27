#!/usr/bin/python3
# -*- coding:utf-8 -*-
import urllib3
urllib3.disable_warnings()

http = urllib3.PoolManager(cert_reqs='CERT_NONE')
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