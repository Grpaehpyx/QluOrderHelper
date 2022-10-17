import datetime
import time

import requests
def fillDataForList(item):
    tempList = {}
    tempList["id"] = item["id"]
    tempList["no"] = item["no"]
#    tempList["name"] = item["name"]
#   tempList["area"] = item["area"]
 #   tempList["category"] = item["category"]
    return tempList
class List:
    def __init__(self,listName):
        self.name=listName
        self.list=[]
    def add(self, obj):
        self.list.append(obj)
def doprint(list):
    print("\t"+list.name,list.list)

param={#二楼借还书 业务接口参数
    'area':'23',
    'segment':'1453007',
    'day':'2022-10-10',
    'startTime':'08:30',
    'endTime':'22:00'
}

header={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'PHPSESSID=tde8pvd5ocbnu93d2kfdv00b91; redirect_url=%2Fhome%2Fweb%2Fseat2%2Farea%2F3%2Fday%2F2022-10-8',
    'Host':'yuyue.lib.qlu.edu.cn',
    'Referer':'http://yuyue.lib.qlu.edu.cn/web/seat3?area=7&segment=1466157&day=2022-10-8&startTime=19:40&endTime=22:00',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
no_idmap={
}










import json
import Utils.TimeUtil as timeUtil
#phpsessionidEqualstr,area,day,startTime,endTime
def getDetailsByCondition(phpsessionidEqualstr='',area='',day='',startTime='',endTime='',floor='',zoneName=''):
    if len(area)>0:param['area']=area
    if len(day)>0:param['day'] = day
    if len(startTime)>0:param['startTime'] = startTime
    if len(endTime)>0:param['endTime'] = endTime

    if day.__lt__(timeUtil.getCurDate()):
        print('day入参不可小于今天')
        return
    import Service.SegmentService as segService##segment需要area和day生成================================
   # print(segService.get_segment(param_day=day,param_area=area))
    param['segment']=segService.get_segment(param_day=day,param_area=area)

    while True:
        try:
            r=requests.get('http://yuyue.lib.qlu.edu.cn/api.php/spaces_old',headers=header,params=param)
            ss=r.json()
            # print(ss)
            #res=json.dumps(ss,sort_keys=True,ensure_ascii=False,indent=4,separators=(',',': '),)

            if(ss['status']==1):
                list=ss["data"]["list"]
                usingList=List("使用中的座位列表")#使用中的座位列表
                emptyList=List('空闲的座位列表')#空闲的座位列表
                orderedList=List('已经被预定的座位列表')#已经被预定的座位列表
                lockedList=List('已经被锁定的座位列表')#已经被锁定的座位列表
                tempLikaiList=List('临时离开的座位列表')#临时离开的座位列表
                allList=List('该区域所有座位列表')#该区域所有的座位列表

                #area_name=list[0]["area_name"]

                for item in list:
                    no_idmap[area+'_'+item['no']]=str(item['id'])
                    tl=fillDataForList(item)
                    allList.add(tl)
                    if item["status_name"]=="使用中":
                        tempList=fillDataForList(item)
                        usingList.add(tempList)
                    elif item["status_name"] == "空闲":
                        tempList=fillDataForList(item)
                        emptyList.add(tempList)
                    elif item["status_name"] == "已预约":
                        tempList=fillDataForList(item)
                        orderedList.add(tempList)
                    elif item["status_name"] == "锁定":
                        tempList=fillDataForList(item)
                        lockedList.add(tempList)
                    elif item["status_name"] == "临时离开":
                        tempList = fillDataForList(item)
                        tempLikaiList.add(tempList)

                print(floor+"楼/"+zoneName+":")
              #  doprint(usingList)
              #  doprint(emptyList)
              #  doprint(orderedList)
              #  doprint(lockedList)
               # doprint(tempLikaiList)
                doprint(allList)
               # printCanbeOrderedList(emptyList)
            else:
                print("获取空间预约信息失败")
            return
        except:continue
def printCanbeOrderedList(emptyList):
    list=[]
    templist=emptyList.list
    for item in templist:
        list.append(item['no'])
    print('以下是您可以预约的位置:')
    print("-------------------")
    index=0
    for item in list:
        index=index+1
        print("%s "%item,end='')
        if index%5==0:print('\n',end='')
    print("\n-------------------",end='')


Id2Area_map={
    '2':['(1)<<===2楼东===>>','(2).<<===2楼西===>>','(3).<<==借还书业务===>'],
    '3':['(1)<<===3楼报刊阅览室===>>','(2)<<===3楼东===>>','(3)<<===3楼西===>>','(4)<<===3楼中走廊===>>'],
    '4':['(1)<<===4楼东===>>','(2)<<===4楼西===>>','(3).<<===4楼中走廊===>>'],
    '5':['(1)<<===5楼东====>>','(2)<<===5楼西===>>','(3).<<===机房===>'],
    '6':['(1)<<===6楼东===>>','(2)<<===6楼西===>>','(3)<<===6楼中厅===>>']
}
#value是areaid,不变化的数据可硬编码,减少网络传输的时间消耗
AreaMap = {
#
# import Service.AreaIdService as areaIdService
# areaList=areaIdService.getAreaIds()
    # {1: '图书馆'}, {2: '二楼'}, {3: '三楼'}, {4: '四楼'}, {5: '2楼东'}, {6: '2楼西'}, {7: '3楼报刊阅览室'},
    # {8: '4楼东'}, {9: '4楼西'}, {10: '4楼中走廊'}, {11: '五楼'}, {12: '六楼'}, {13: '3楼东'}, {16: '5楼东'},
    # {17: '5楼西'}, {18: '6楼西'}, {19: '6楼东'}, {20: '6楼中厅'}, {21: '3楼西'}, {22: '3楼中走廊'},
    # {23: '借还书业务'}, {24: '机房'}
    '21':'5',
    '22':'6',
    '23':'23',
    '31':'7',
    '32':'13',
    '33':'21',
    '34':'22',
    '41':'8',
    '42':'9',
    '43':'10',
    '51':'16',
    '52':'16',
    '53':'24',
    '61':'19',
    '62':'18',
    '63':'20'
}
# time1=time.perf_counter()
# for k,v in AreaMap.items():
#     getDetailsByCondition(phpsessionidEqualstr='',area=v,day='2022-10-13',startTime='08:30',endTime='22:00',floor=k[0],zoneName=Id2Area_map[k[0]][int(k[1])-1])
#
# time2=time.perf_counter()
# print(time2-time1)
# print(no_idmap)
#getDetailsByCondition(phpsessionidEqualstr='',area='23',day='2022-10-14',startTime='18:00',endTime='22:00',floor='2',zoneName='<<==借还书业务===>')

#http://yuyue.lib.qlu.edu.cn/api.php/areas/0/date/2022-10-10 get 获得每个地方的areaid


# window.ska = {
#     'bookRule': "zh" == "en"?[""]: [
#     'backUrl': "/web/index",
# 'parentUrl': "/web/seat",
# 'areaUrl': "/web/seat3",
# 'dayApi': "/api.php/space_days",
# 'timeApi': "/api.php/space_time_buckets",
# 'usersApi': "/api.php/users",
# 'spacesApi': "/api.php/spaces",
# 'areaApi': "/api.php/areas",
# 'areadaysApi': "/api.php/areadays",
# 'loginApi': "/api.php/login",
# 'logoutApi': "/api.php/logout",
# 'access_token': "28e0bb1b976c0ab4b81e87dadad600f9",
# 'userid': "201911010012",
# 'username': "郑雄",
# 'checkUrl': "/api.php/check",
# 'heatColor': {"1": "#00B831", "2": "#22CB10", "3": "#51CB10", "4": "#9ECB10", "5": "#CBB910", "6": "#CB7A10",
#               "7": "#CB5B10", "8": "#CB3C10", "9": "#CB1D10", "10": "#AF001F", "11": "#8B8B8B"}};


#结束上次定时器 889hang in  common.js