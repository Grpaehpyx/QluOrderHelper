import requests
import entity.ParamAndConfig as config
header={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie': 'uservisit=1; redirect_url=%2Fweb%2Findex',
    'Host': 'yuyue.lib.qlu.edu.cn',
    'Referer': 'http://yuyue.lib.qlu.edu.cn/web/notopen',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
def getCookies():
    while True:
        try:
            r=requests.get('http://yuyue.lib.qlu.edu.cn/web/index',headers=header)
            print('第一次访问的header',r.headers)
            cookies={}
            cookies['PHPSESSID']=r.cookies['PHPSESSID']
            config.set_value('firstqueryid',r.cookies['PHPSESSID'])
            print(r.cookies['PHPSESSID'])
            cookies['redirect_url']=r.cookies['redirect_url']
            return cookies
        except:
            continue