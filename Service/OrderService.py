import time
import Utils.TimeUtil as timeutil

import requests
header={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '88',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'userid=201911010012; uservisit=1',
    'Host': 'yuyue.lib.qlu.edu.cn',
    'Origin': 'http://yuyue.lib.qlu.edu.cn',
    'Referer': 'http://yuyue.lib.qlu.edu.cn/web/seat3?area=23&segment=1453007&day=2022-10-14&startTime=08:30&endTime=22:00',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
formdata={
            'access_token': 'da69ee878a176046bf7652799158d78c',
            'userid': '201911010012',
            'segment': '1453006',
            'type': '1'
         }

def settoken(token):
    formdata['access_token']=token
def setcookie(cookie):##PHPSESSID，access_token
    str=header['Cookie']
    str=str+"; "+cookie
    header['Cookie'] = str  # 覆盖
def getcookie():
    return header['Cookie']

#7879 8178
# 300
#8179
def order(access_token='',formdata_userid='',formdata_seg=0,php_sessionid='',realsiteId='7978'):#seg需要通过area和day组合请求得到
    if len(access_token)>0:
        formdata['access_token']=access_token
        setcookie('access_token='+'='+access_token)
    if len(formdata_userid)>0:
        formdata['userid']=formdata_userid
    #if formdata_seg>0:
    formdata['segment']=formdata_seg
    if len(php_sessionid)>0:
        setcookie('PHPSESSID'+'='+php_sessionid)

    url='http://yuyue.lib.qlu.edu.cn/api.php/spaces/'+realsiteId+'/book'
    trynum=0
    orderflag=0
    while orderflag==0 and trynum<2000 :
        try:
            r=requests.post(url,headers=header,data=formdata)
            jsonstr=r.json()
            #print(jsonstr)
            #print(jsonstr['msg'])
            print('用户%s登入凭证过期时间:%s'%(jsonstr['data']['_hash_']['userid'],jsonstr['data']['_hash_']['expire']))
            # import json
            # res = json.dumps(jsonstr, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '), )
            # print(res)

            if(jsonstr['msg']=='预约成功'):
                print("预约成功====================")
                orderflag=1
            else:
                trynum=trynum+1
                print(jsonstr['msg'])
                print(header)
                print(formdata)
                time.sleep(0.7)
                print(timeutil.getCurDateAndTime(),'尝试第%d次预约======================================='%trynum)
        except:
            continue
#order(realsiteId='123')

##7879 -8178二楼借还书
#7863-7878二楼西
#5735-5750二楼东
#6027-6042三楼西
#6027-6042三楼东