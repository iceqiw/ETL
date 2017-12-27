#!/usr/bin/env python3
#coding: utf-8

import smtplib
import email.mime.multipart  
import email.mime.text
from Models import send_cfg

def runSend(train):
    if train['hard_sleeper'] == '无':
        print('-----------------------raise-----------------------')
        return
    
    for s in send_cfg.select():
        sendEmail(train,s)


def sendEmail(train,cfg):
    subject = '火车票通知:'
    print('-----------------------sendEmail-----------------------')
    msg = email.mime.multipart.MIMEMultipart()  
    msg['Subject'] = subject+train['end']
    msg['From'] = cfg.sender
    msg['To'] =cfg.receiver   
    content = ''' 
        tongzhi ,huochepiao
        这是一封自动发送的邮件。 
        http://106.14.188.143
    '''  
    txt = email.mime.text.MIMEText(content)  
    msg.attach(txt)  
    smtp = smtplib.SMTP_SSL()
    smtp.connect('smtp.163.com',465)
    smtp.login(cfg.sender, cfg.password)
    smtp.sendmail(cfg.sender, cfg.receiver, msg.as_string())
    smtp.quit()
    print('-----------------------ok-----------------------')
