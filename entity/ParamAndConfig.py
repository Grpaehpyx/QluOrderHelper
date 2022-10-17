def _init():
    global _global_configPool
    _global_configPool={}
def set_value(key,value):
    _global_configPool[key]=value
def get_value(key):
    try:
        return _global_configPool[key]
    except:
        print('读取'+key+'失败')
def getSizeOfPool():
    return len(_global_configPool)
def get_global_pool():
    return _global_configPool




class CancelOrderParam:
    def __init__(self,url,reqMethod,method,id,userid,access_token):
        self.reqUrl =url
        self.reqMethod=reqMethod
        self.datamap={}
        self.datamap['_method']=method
        self.datamap['id']=id
        self.datamap['userid']=userid
        self.datamap['access_token']=access_token
        self.reqHeader={}#解析获得再填充
    def fillReqHeader(self,headmap):
        self.reqHeader=headmap
    def fillReqUrl(self,url):
        self.reqUrl=url



import Utils.TimeUtil as timeutil
class PersonConfig:
    def __init__(self,username,password,flow='',day='',startTime=timeutil.getDefaultStartTime(),endTime=timeutil.getDefaultEndTime(),verify=''):
        self.username=username
        self.password=password
        self.flow=flow
        self.day=day
        self.startTime=startTime
        self.endTime=endTime
        self.verify=verify

