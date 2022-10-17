import requests


data={
    'username':'201911010012',
    'password':'qlu162315',
    'verify':'2064',
    'PHPSESSID':'4d9hhd6qu8vt30gtvu7sqsh0f7'

}

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34',
    'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Cookie':'PHPSESSID=fs66ink5dquvju64svg5nitkg4; redirect_url=%2Fweb%2Findex',
    'Host':'yuyue.lib.qlu.edu.cn',
    'Referer':'http://yuyue.lib.qlu.edu.cn/web/index'
}

header2={
#GET /api.php/areas/3/date/2022-10-7 HTTP/1.1
'Accept':'*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': 'PHPSESSID=tde8pvd5ocbnu93d2kfdv00b91; redirect_url=%2Fhome%2Fweb%2Fseat2%2Farea%2F3%2Fday%2F2022-10-7; userid=201911010012; user_name=%E9%83%91%E9%9B%84; access_token=ae96db28b56d85597115d05a2590aa30; expire=2022-10-08+16%3A48%3A22',
'Host': 'yuyue.lib.qlu.edu.cn',
'Referer':'http://yuyue.lib.qlu.edu.cn/home/web/seat2/area/3/day/2022-10-7',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}

#r=requests.post('http://yuyue.lib.qlu.edu.cn/api.php/login',data=data)
#r=requests.post('http://yuyue.lib.qlu.edu.cn/api.php/check?0.1359160675833293&random=0.3257384625531863&random=0.6400378228844374&random=0.8948674380853814&random=0.00615692188583794&random=0.5368289950232745',data=data)
#r=requests.get('http://yuyue.lib.qlu.edu.cn/api.php/check?0.5487645569781112',headers=header,data=data)
#r=requests.get('http://yuyue.lib.qlu.edu.cn/web/index')
#http://yuyue.lib.qlu.edu.cn/api.php/check?0.5487645569781112

import json

r=requests.get('http://yuyue.lib.qlu.edu.cn/api.php/areas/3/date/2022-10-8',headers=header2)
ss=r.json()
print(ss)
res=json.dumps(ss,sort_keys=True,ensure_ascii=False,indent=4,separators=(',',': '),)
print(res)


childArea=ss["data"]["list"]["childArea"]
print(ss["data"]["list"]["childArea"])
dic={}
for item in childArea:
    key=item["name"]
    # print(item["TotalCount"])
    # print(item["UnavailableSpace"])
   # dic[key]=int(item["TotalCount"])-int(item["UnavailableSpace"])
    dic[key]=item["TotalCount"]-item["UnavailableSpace"]

print(dic)
#print(r.json())
#
# with open('abc.png','wb') as f:
#     f.write(r.content)
# print(r.text)
# s='u\u5f02\u5e38\u8bbf\u95ee'
# print(s)
