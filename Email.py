#!/usr/bin/env python3
#coding: utf-8

import smtplib
import email.mime.multipart  
import email.mime.text

sender = '*******@163.com'
receiver = '*******@qq.com'
subject = '火车票通知:'
password = '*********'

def sendEmail(end):
    msg = email.mime.multipart.MIMEMultipart()  
    msg['Subject'] = subject+end
    msg['From'] = sender
    msg['To'] =receiver   
    content = ''' 
        tongzhi ,huochepiao
        这是一封自动发送的邮件。 
        http://106.14.188.143
    '''  
    txt = email.mime.text.MIMEText(content)  
    msg.attach(txt)  

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com','25')
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('-----------------------ok-----------------------')
