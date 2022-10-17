def _init():
    global _global_userPool
    _global_userPool={}
def set_user(key,user):
    _global_userPool[key]=user
def get_value(key):
    try:
        return _global_userPool[key]
    except:
        print('读取'+key+'失败')
def getSizeOfPool():
    return len(_global_userPool)
def get_global_pool():
    return _global_userPool


class User:
    def __init__(self,access_token=None,expire=None,userid=None,deptName=None,gender=None,joinTime=None,mobile=None,name=None,roleName=None,status=None):
        self.access_token=access_token
        self.expire=expire
        self.userid=userid

        self.deptName=deptName
        self.gender=gender
        self.joinTime=joinTime
        self.mobile=mobile
        self.name=name
        self.roleName=roleName
        self.status=status

        self.siteIds=[]#需要预约的位置id
    def append(self,siteids):
        for item in siteids:
            self.siteIds.append(item)


#{
#     "data": {
#         "_hash_": {
#             "access_token": "0d0c29ba49c7c458d16debaf8b83ecfb",
#             "expire": "2022-10-09 10:17:00",
#             "userid": "201911010012"
#         },
#         "list": {
#             "ROW_NUMBER": "1",
#             "birthday": "",
#             "card": "1507143335",
#             "consumeScore": 0,
#             "dept": null,
#             "deptName": "数学与统计学院",
#             "email": "",
#             "fillScore": 0,
#             "gender": 1,
#             "hw_update_flag": 1,
#             "id": "201911010012",
#             "idCard": "162315",
#             "joinTime": "2020-08-17 20:30:16",
#             "mobile": "17679179448",
#             "name": "郑雄",
#             "qq": "",
#             "renegeinfo": null,
#             "role": null,
#             "roleName": "本科",
#             "saving": ".0000",
#             "skedb_update_flag": 1,
#             "status": 1,
#             "subDept": null,
#             "subDeptName": null,
#             "tel": "",
#             "totalConsumeScore": 0,
#             "totalFillScore": 0,
#             "wallet": ".0000",
#             "weixin": ""
#         }
#     },
#     "msg": "登陆成功",
#     "status": 1
# }