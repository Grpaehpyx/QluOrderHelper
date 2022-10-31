import requests
import json

data={
    'username':'',
    'password':'',
    'verify':'2064',
    'PHPSESSID':'4d9hhd6qu8vt30gtvu7sqsh0f7'

}

header={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '52',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'PHPSESSID=tde8pvd5ocbnu93d2kfdv00b91; uservisit=1; redirect_url=%2Fhome%2Fweb%2Fseat%2Farea%2F1',
    'Host': 'yuyue.lib.qlu.edu.cn',
    'Origin': 'http://yuyue.lib.qlu.edu.cn',
    'Referer': 'http://yuyue.lib.qlu.edu.cn/home/web/seat/area/1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}

r=requests.post('http://yuyue.lib.qlu.edu.cn/api.php/login',headers=header)

ss=r.json()
print(ss)

res=json.dumps(ss,sort_keys=True,ensure_ascii=False,indent=4,separators=(',',': '),)
print(res)


