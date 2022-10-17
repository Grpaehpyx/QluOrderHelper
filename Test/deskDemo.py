# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/13 上午 04:01
@Auth ： zhengxiong
@File ： deskDemo.py
@QQ ：   2736590207
    """

import threading
import schedule
import time
import Utils.TimeUtil as  timeutil
def job():
    num=0
    while num<5:
        num=num+1
        print("当前时间%s,I'm working..."%timeutil.getCurDateAndTime())
        time.sleep(0.5)
#schedule.every(1).seconds.do(job)
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("05:40").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)
# while True:
schedule.run_pending()
print(timeutil.getCurDateAndTime())
time.sleep(1)
#    time.sleep(1)
 #   print(timeutil.getCurDateAndTime())
# import schedule
# import time
# import threading
#
# def job():
#     print("I'm working... in job1  start")
#     time.sleep(15)
#     print("I'm working... in job1  end")
#
# def job2():
#     print("I'm working... in job2")
#
# def run_threaded(job_func):
#      job_thread = threading.Thread(target=job_func)
#      job_thread.start()
#
# schedule.every(2).seconds.do(run_threaded,job)
# schedule.every(3).seconds.do(run_threaded,job2)
#
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)