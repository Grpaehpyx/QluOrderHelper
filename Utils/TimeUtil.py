# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/9 下午 05:50
@Auth ： zhengxiong
@File ： TimeUtil.py
@QQ ：   2736590207
"""
import datetime
#http://yuyue.lib.qlu.edu.cn/api.php/areas/0/date/2022-10-10 get 获得每个地方的areaid
import time

def getCurDate():
    return time.strftime('%Y-%#m-%#d',time.localtime())
def getTomorrowData():
    #获取当天日期
    import datetime
    now_time = datetime.datetime.now()
    res=((now_time + datetime.timedelta(days=+1)).strftime("%Y-%#m-%#d"))  # 获取后一天
    return res
def getpostData(i):
    #获取当天日期
    import datetime
    now_time = datetime.datetime.now()
    res=((now_time + datetime.timedelta(days=+i)).strftime("%Y-%#m-%#d"))  # 获取后一天
    return res

def getCurTime():
    return time.strftime('%H:%M', time.localtime())
def getCurDateAndTime():
    return time.strftime('%Y-%#m-%#d %H:%M:%S',time.localtime())



def getDefaultStartTime():
    return time.strftime('08:30',)
def getDefaultEndTime():
    return time.strftime('22:00')
# print("请输入数字选择日期=========================================================")
# print('(1)<<===%s===>>'%(getCurDate()))
# print('(1)<<===%s===>>'%(getTomorrowData()))
# d1=datetime.date(2022,10,12)
# d2=datetime.date(2022,10,11)
# d3=time.strftime('%Y-%#m-%#d',time.localtime())
# d4=datetime.date(2022,10,9)
# print(d3.__le__(str(d4)))

#print('2022-10-11'.__le__(getTomorrowData()))
def do(x):
    print(123)
    if x>1:return
    print(1233)
