# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/9 下午 06:15
@Auth ： zhengxiong
@File ： AreaIdService.py
@QQ ：   2736590207
"""
#http://yuyue.lib.qlu.edu.cn/api.php/areas/0/date/2022-10-10 get 获得每个地方的areaid
header={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'PHPSESSID=ka2sepj91097dbcd4dkkicalk0; access_token=4a5e9168c476c1f4cf41109fb5eaec2b',
    'Host': 'yuyue.lib.qlu.edu.cn',
    'Referer': 'http://yuyue.lib.qlu.edu.cn/home/web/seat/area/1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
#'Cookie':'PHPSESSID=t2ahq8u7pmlptsvt2jbuo8seg5; userid=201911010012; user_name=%E9%83%91%E9%9B%84; uservisit=1; access_token=28e0bb1b976c0ab4b81e87dadad600f9; expire=2022-10-09+18%3A47%3A11; redirect_url=%2Fhome%2Fweb%2Fseat%2Farea%2F1',

import requests
import json
def getAreaIds(str=''):##PHPSESSID access_token
    print("获取区域ids中============")
    if len(str)>0:
        header['Cookie']=str
    r=requests.get('http://yuyue.lib.qlu.edu.cn/api.php/areas/0/date/2022-10-11',headers=header)
    jsonstr=r.json()
    print(jsonstr)

    orginlist=jsonstr['data']['list']['childArea']
    resList=[]
    for item in orginlist:
        tempdic={}
        tempdic[item['id']]=item['name']
        resList.append(tempdic)
    # formatRes=json.dumps(jsonstr,ensure_ascii=False,sort_keys=True, indent=4, separators=(',', ': '), )
    # print(formatRes)
    return resList
list=getAreaIds()
print(list)