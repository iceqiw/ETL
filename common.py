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
    "JSESSIONID=D8F410CA7F4C9F56DE7C3D62DB898E86; _jc_save_detail=true; RAIL_OkLJUJ=FFB2V0iAeAjwLyc10PPqi6w7T9pGMmAO; fp_ver=4.5.1; RAIL_EXPIRATION=1505014513552; RAIL_DEVICEID=itvSDLsvzejr7dfkjxqu0e2xdz91iSG65yjk-Do5ocN81JY3O_ljXsi-ThJOm5_tmQQC07sXwNuihXPQRd03EvDqeR2Z_AkgPBdDQSScBUikITPy4o3sBWKyXy3I0_g9m0COBAanlscLrFNIDtcybTjiJWg9a1mT; _jc_save_showIns=true; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=417857802.50210.0000; BIGipServerpassport=837288202.50215.0000; _jc_save_fromStation=%u897F%u5B89%2CXAY; _jc_save_toStation=%u798F%u5DDE%2CFZS; _jc_save_fromDate=2017-10-06; _jc_save_toDate=2017-09-08; _jc_save_wfdc_flag=dc"
}