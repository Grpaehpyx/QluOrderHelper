import requests
header={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=ka2sepj91097dbcd4dkkical0; userid=201911010012; user_name=%E9%83%91%E9%9B%84; uservisit=1; access_token=98e5d35c98acad367081dfe2b4cafd; expire=2022-10-09+17%3A45%3A29; redirect_url=%2Fweb%2Fseat2%2Farea%2F2%2Fday%2F2022-10-10',
    'Host': 'yuyue.lib.qlu.edu.cn',
    'Referer': 'http://yuyue.lib.qlu.edu.cn/web/seat2/area/2/day/2022-10-9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
param={
            'day': '2022-10-12',
            'area': '10',
         }

import json
# r=requests.get('http://yuyue.lib.qlu.edu.cn/home/web/index')
# h=r.headers
#
# print(h)
# print(h['Set-Cookie'])
#
# res=h['Set-Cookie'].split(";")
# print(res[0])
#
# header['Cookie']=header['Cookie']+"; "+res[0]
# print(header['Cookie'])
#

def get_segment(param_day,param_area):##不需要phpsession和access_token
    while True:
        try:
            param['day']=param_day
            param['area']=param_area

            r=requests.get('http://yuyue.lib.qlu.edu.cn/api.php/space_time_buckets',headers=header,params=param)
            jsonstr=r.json()
            #print(jsonstr)
            #
            # import json
            # res = json.dumps(jsonstr, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '), )
            # print(res)
            #print(jsonstr['data']['list'][0]['id'])


            ans=jsonstr['data']['list'][0]['id']
            if(jsonstr['status']==1):
                print("成功获取seg:",ans)
                print("seg类型:",type(ans))
                return ans
            else:
                print("获取seg失败,msg:",jsonstr['msg'])
        except:continue
 # //获取可用时间段
 #        var area_times=get_area_time(day,areaId,ska.timeApi);
 #        var timeSegment;
 #        var firstSegment;
	# 	if(area_times.status == 1){
	# 	    timeSegment = area_times.data.list;
	# 	    firstSegment = $.isArray(timeSegment)?timeSegment[0]['id']:0;
 #        }
#print(get_segment('2022-10-13','7'))