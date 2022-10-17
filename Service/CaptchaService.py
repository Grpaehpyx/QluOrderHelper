import requests
import random
header = {
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'uservisit=1',
        'Host': 'yuyue.lib.qlu.edu.cn',
        'Referer': 'http://yuyue.lib.qlu.edu.cn/home/web/seat/area/1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
#'PHPSESSID=tde8pvd5ocbnu93d2kfdv00b91;不用这个也行

def setcook(verify):
    str = header['Cookie']
    str = str + "; " + verify
    header['Cookie'] = str  # 覆盖

def getCaptchaAndSave():
    while True:
        try:
            flag=0
            num=0
            while flag==0 and num<100:
                try:
                    print("获取验证码ing")
                    r=requests.get('http://yuyue.lib.qlu.edu.cn/api.php/check',headers=header)
                    if r.status_code==200:
                         break

                except:
                    num = num + 1
                    print("尝试第%d次获取验证码=========="%num)
                    continue
                #print(r.headers)
            num=random.randint(1,200)
            path='abc'+str(num)+'.png'
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
            print("成功爬取验证码:"+path+"===============")
            return path
        except:continue