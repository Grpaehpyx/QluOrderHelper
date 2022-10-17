# #人工识别
import json
data={'status': 1, 'msg': '登陆成功', 'data': {'list': {'id': '201911010012', 'card': '1507143335', 'name': '郑雄', 'idCard': '162315', 'gender': 1, 'birthday': '', 'joinTime': '2020-08-17 20:30:16', 'wallet': '.0000', 'saving': '.0000', 'fillScore': 0, 'totalFillScore': 0, 'consumeScore': 0, 'totalConsumeScore': 0, 'role': None, 'roleName': '本科', 'dept': None, 'deptName': '数学与统计学院', 'subDept': None, 'subDeptName': None, 'tel': '', 'mobile': '17679179448', 'email': '', 'qq': '', 'status': 1, 'weixin': '', 'hw_update_flag': 1, 'skedb_update_flag': 1, 'ROW_NUMBER': '1', 'renegeinfo': None}, '_hash_': {'userid': '201911010012', 'access_token': '5b9180c7a203ce3bc57fd5984f9210d3', 'expire': '2022-10-09 03:38:14'}}}
res = json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '), )
print(res)
