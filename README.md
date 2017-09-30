12306

conf.py 配置邮件，车站信息
定时任务命令


crontab -l
crontab -e

*/1 * * * * /root/ETL/Trains.py >> /root/train.log

service crond start