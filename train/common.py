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
    "JSESSIONID=5EC5B12A73DC6D000484A99FCCD747FD; _jc_save_detail=true; RAIL_OkLJUJ=FFB2V0iAeAjwLyc10PPqi6w7T9pGMmAO; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=2045247754.24610.0000; BIGipServerpassport=937951498.50215.0000; RAIL_EXPIRATION=1510445794929; RAIL_DEVICEID=akRjCfxqcpM2fMOAqm4CJZzidINzPVjLTZUAJrs1Ll9h6UEosMCFKmdzs7P6rs2kQKbV9hgdjes1GXzlmYyMY8HRHe6tLjTviB9b6U6tO6vLwQelergVyuvD-barRmYQYB1_7iVm0FJ10cGgspHJGhFSygFjD-Zf; _jc_save_fromStation=%u798F%u5DDE%2CFZS; _jc_save_toStation=%u897F%u5B89%2CXAY; _jc_save_fromDate=2017-11-10; _jc_save_toDate=2017-11-08; _jc_save_wfdc_flag=dc"
}