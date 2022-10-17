import requests
header={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '52',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'uservisit=1',
    'Host': 'yuyue.lib.qlu.edu.cn',
    'Origin': 'http://yuyue.lib.qlu.edu.cn',
    'Referer': 'http://yuyue.lib.qlu.edu.cn/home/web/seat/area/1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
formdata={
                'username':'201911010012',
                'password':'qlu162315',
                'verify':1234
         }




def setcookie(cookie):
    str=header['Cookie']
    str=str+"; "+cookie
    header['Cookie'] = str  # 覆盖

def login(username,password,verify):
    formdata['username']=username
    formdata['password']=password
    formdata['verify']=verify
    r=requests.post('http://yuyue.lib.qlu.edu.cn/api.php/login',headers=header,data=formdata)
    print(r.headers)
    jsonstr=r.json()
    print(jsonstr)

    import json
    res = json.dumps(jsonstr, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '), )
    print(res)


    if jsonstr['msg']== '登陆成功':
        print("登入成功====================")
        print("正在保存您的信息============= ")
        save(jsonstr)
        print("保存成功====================")
        return 1
    else:
        print(jsonstr['msg'],"登入失败=====")
        return 0
def save(jsonstr):
    import entity.UserMoudle as userhander
    sex ='男' if jsonstr['data']['list']['gender']==1 else '女'
    tempuser=userhander.User(access_token=jsonstr['data']['_hash_']['access_token'],
                             expire=jsonstr['data']['_hash_']['expire'],
                             userid=jsonstr['data']['_hash_']['userid'],
                             deptName=jsonstr['data']['list']['deptName'],
                             gender=sex,
                             joinTime=jsonstr['data']['list']['joinTime'],
                             mobile=jsonstr['data']['list']['mobile'],
                             name=jsonstr['data']['list']['name'],
                             roleName=jsonstr['data']['list']['roleName'],
                             status=jsonstr['status']
                             )

    userhander.set_user(tempuser.userid,tempuser)
    print('当前用户池大小=',userhander.getSizeOfPool())
#login('201911010018','qlu156116',)