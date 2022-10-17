# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/10 下午 04:15
@Auth ： zhengxiong
@File ： User.py
@QQ ：   2736590207
"""

class User:
    def __init__(self):
        self.data={}
        self.msg=None
        self.status=None
    def setdata(self,data):
        self.data=data
    def setmsg(self,msg):
        self.msg=msg
    def setstatus(self,status):
        self.status=status
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