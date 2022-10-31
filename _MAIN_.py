# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/9 下午 11:53
@Auth ： zhengxiong
@File ： _MAIN_.py
@QQ ：   2736590207
"""
import time
import Utils.TimeUtil as timeutil
import Service.FristQuery as firstQuery
import Service.LoginService as loginService
import QueryEmpty
import Service.CaptchaService as capService
import Service.OrderService as orderService
import entity.ParamAndConfig as config
config._init()
import entity.UserMoudle as userhander
userhander._init()
import Service.ShowPicService as showpic

Id2Area_map={
            '2':['(1)<<===2楼东===>>','(2).<<===2楼西===>>z','(3).<<==借还书业务===>'],
            '3':['(1)<<===3楼报刊阅览室===>>','(2)<<===3楼东===>>','(3)<<===3楼西===>>','(4)<<===3楼中走廊===>>'],
            '4':['(1)<<===4楼东===>>','(2)<<===4楼西===>>','(3).<<===4楼中走廊===>>'],
            '5':['(1)<<===5楼东====>>','(2)<<===5楼西===>>','(3).<<===机房===>'],
            '6':['(1)<<===6楼东===>>','(2)<<===6楼西===>>','(3)<<===6楼中厅===>>']
            }
#value是areaid,不变化的数据可硬编码,减少网络传输的时间消耗
AreaMap = { # {1: '图书馆'}, {2: '二楼'}, {3: '三楼'}, {4: '四楼'}, {5: '2楼东'}, {6: '2楼西'}, {7: '3楼报刊阅览室'},
            # {8: '4楼东'}, {9: '4楼西'}, {10: '4楼中走廊'}, {11: '五楼'}, {12: '六楼'}, {13: '3楼东'}, {16: '5楼东'},
            # {17: '5楼西'}, {18: '6楼西'}, {19: '6楼东'}, {20: '6楼中厅'}, {21: '3楼西'}, {22: '3楼中走廊'},
            # {23: '借还书业务'}, {24: '机房'}
            '21':'5','22':'6','23':'23',    '31':'7','32':'13','33':'21','34':'22',
            '41':'8','42':'9','43':'10',      '51':'16','52':'16','53':'24',  '61':'19','62':'18','63':'20'
          }

siteIdmap = {
            '5_001': '5735', '5_016': '5750',   '6_001': '7863', '6_016': '7878',   '23_001': '7879', '23_300': '8178',
             '7_001': '5767','7_144': '5910',  '7_089': '8294','7_092': '8297',    '13_001': '5911', '13_116': '6026',
            '21_001': '6027', '21_016': '6042',      '22_001': '6043', '22_072': '6114',
            '8_001': '6115', '8_116': '6230',        '9_001': '6231', '9_016': '6246',
            '10_001': '6247', '10_080': '6326',      '16_001': '6327', '16_392': '6718',
            '24_001': '8179', '24_099': '8277',      '19_001': '6863', '19_456': '7318',
            '18_001': '7319', '18_456': '7774',      '20_001': '7775', '20_088': '7862'
           }

def main():
    global username
    global password
    print(timeutil.getCurDateAndTime(),"<<==欢迎使用图书馆自动预约系统==>>")
    print("\n友情提示/预约相关:==========================================")
    print("(0).图书馆预约系统服务时间为每天6.00-24.00,")
    print("你可以在每天这个时间段预约当天的位置(需在30min内去签到),"
          "也可预约第二天的位置(第二天9点前签到)")
    print("此系统最大作用在于帮你预约第二天的位置,\n官方渠道得每天早上6点起来抢位置,"
          "使用本系统,\n你只需要配置好相关信息,它将自动帮你抢座,\n解放你的双手,助你睡个好觉!")
    print("(1).自动预约功能需要输入账号,密码和时间段三部分必要信息")
    print("(2).预约当天的座位将立刻生效,\n请在30分钟内持校园卡或NFC设备,\n在图书馆一楼刷卡签到，超时后将会被记录违约1次")
    print("(3).预约第二天的座位.自动预约功能需要输入账号,密码和时间段三部分必要信息,")
    print("\n友情提示/取消预约相关:=======================================")
    print("(0).当天预约的座位没办法线上取消,只能去门口签到再签退")
    print("(1).当天预约的第二天的座位可在第二天9点前线上取消,\n\n")

    print(timeutil.getCurDateAndTime(),"<<==请输入对应数字选择你的操作==>>")
    print("1<===>查询当前空闲位置")
    print("2<===>配置自动预约")
    print("3<===>查看/取消预约")
    print("4<===>查看个人资料")

    opt=input("请从1/2/3/4中选择输入")
    import QueryEmpty as queryempty
    if(opt=='1'):
        queryempty.getDetailsByCondition()
    elif(opt=='2'):

        cookies = firstQuery.getCookies()#{}第一次访问的phpSessionid
        capService.setcook('PHPSESSID=' + config.get_value('firstqueryid'))
        # 设置登入服务的cook
        loginService.setcookie('PHPSESSID=' + config.get_value('firstqueryid'))

        loginflag=0
        while loginflag==0:

            print()
            username = input("请输入你的学号:\n")
            password = input("请输入你的密码:\n")

            path=capService.getCaptchaAndSave()  # 获取验证码
            import _thread as th
            try:
                th.start_new_thread(showpic.showpicture,(path,))#另外起一个线程,不然会一直阻塞在plt的show函数,直到关闭窗口
            except:
                print("Error: 无法启动线程")


            verify = input("请输入验证码\n")
            personconfig=config.PersonConfig(username=username,password=password,verify=verify)
            config.set_value(username,personconfig)#全局配置池,缓存用户信息

            # 登入服务======================================================================
            print("登入ing=================================================================")
            print("您可将本系统看作您的另一台设备,如果账号已经处于登入状态,再次登入时会将别的设备的账号挤下去")
            loginflag=loginService.login(config.get_value(username).username, config.get_value(username).password, config.get_value(username).verify)

        print("========================================================")
        print("(2)<<===二楼===>>")
        print("(3)<<===三楼===>>")
        print("(4)<<===四楼===>>")
        print("(5)<<===五楼===>>")
        print("(6)<<===六楼===>>")
        xuanzeflag=0

        curlist=None
        floor=None
        while xuanzeflag==0:
            floor=input("请输入数字选择楼层===================================================\n")
            try:
                curlist = Id2Area_map[floor]
                xuanzeflag=1
            except:
                print('输入有误,请重新输入')
        for item in curlist:
            print(item)
        zone=input("请输入数字选择区域====================================================\n")

        zoneparam=(int(zone) - 1)

        fz=floor+zone#几楼哪个区域！！！！下方接口参数2
        import Utils.TimeUtil as timeUtil
        print("请输入数字选择日期=========================================================")
        print('(1)<<===预约今天%s的位置!===>>'%(timeUtil.getCurDate()))
        print('(1)<<===预约明天%s的位置!===>>'%(timeUtil.getTomorrowData()))
        print('(2)<<===后天%s至未来一周,可自由选择哪几天===>>\n'%(timeUtil.getpostData(2)))
        #入参填充========================================================================
        day=''#日期
        while True:

            day=input()
            if(day=='1'):
                print('你已经选择了今天%s 时间段%s-%s'%(timeUtil.getCurDate(),timeUtil.getCurTime(),timeUtil.getDefaultEndTime()))
                break
            elif(day=='2'):
                print('你选择了明天%s 时间段%s-%s'%(timeUtil.getTomorrowData(),timeUtil.getDefaultStartTime(),timeUtil.getDefaultEndTime()))
                break
            elif(day=='3'):
                print('你选择了明天%s 时间段%s-%s'%(timeUtil.getTomorrowData(),timeUtil.getDefaultStartTime(),timeUtil.getDefaultEndTime()))
                print('(0)<<===%s===>>'%timeutil.getpostData(1))
                print('(1)<<===%s===>>'%timeutil.getpostData(2))
                print('(2)<<===%s===>>'%timeutil.getpostData(3))
                print('(3)<<===%s===>>'%timeutil.getpostData(4))
                print('(4)<<===%s===>>'%timeutil.getpostData(5))
                print('(5)<<===%s===>>'%timeutil.getpostData(6))
                inp=input('现在是%s,请输入数字选择哪几天需要自动抢座,数字之间以空格隔开'%timeutil.getTomorrowData())
                li=list(map(int, inp.split()))

                userhander.User(userhander.get_value(username)).append(li)

                break
            else:
                print('输入异常,请重新输入,只能输入数字1,2,3')
        #return
        dayparam=None
        if day=='1':
            dayparam = timeUtil.getCurDate()
        elif day == '2':
            dayparam=timeUtil.getTomorrowData()
        else:
            dayparam=timeUtil.getTomorrowData()#下方接口参数3
        startTimeParam=''#下方接口参数4
        endTimeParam=''#下方接口参数5
        if(day=='1'):
            startTimeParam=timeUtil.getCurTime()
            endTimeParam=timeUtil.getDefaultEndTime()
        else:
            startTimeParam='8:30'
            endTimeParam='22:00'

        print("查询日期:%s 时间段:%s-%s 的可用座位中================================="%(dayparam,startTimeParam,endTimeParam))
        QueryEmpty.getDetailsByCondition(phpsessionidEqualstr='PHPSESSID'+'='+config.get_value('firstqueryid'),area=AreaMap[fz],day=dayparam,startTime=startTimeParam,endTime=endTimeParam,floor=floor,zoneName=Id2Area_map[floor][zoneparam])

        siteNo=int(input("请输入数字选择你要预约的座位\n"))



        print("预约ing============")

        import Service.SegmentService as segService
        seg=segService.get_segment(dayparam,AreaMap[fz])#day和areaid

        realsite=str(int(siteIdmap[AreaMap[fz]+'_001'])+siteNo-1)

        import schedule
        schedule.every().day.at("05:59").do(orderService.order,realsiteId=realsite, access_token=userhander.get_value(username).access_token,
                           formdata_userid=username, formdata_seg=seg, php_sessionid=config.get_value('firstqueryid'))
        schedule.every(1).seconds.do(orderService.order, realsiteId=realsite,
                                            access_token=userhander.get_value(username).access_token,
                                            formdata_userid=username, formdata_seg=seg,
                                            php_sessionid=config.get_value('firstqueryid'))




        while True:
            schedule.run_pending()
            print('当前时间:',timeutil.getCurDateAndTime())
            time.sleep(1)
    elif(opt=='3'):
        print(3)
    elif(opt=='4'):
        print(2)

main()

# import schedule
# def job(realsiteId, access_token,formdata_userid, formdata_seg, php_sessionid):
#     orderService.order(realsiteId=realsiteId, access_token=access_token,formdata_userid=formdata_userid, formdata_seg=formdata_seg, php_sessionid=php_sessionid)
#     time.sleep(0.5)
#     print("当前时间%s,I'm working..."%timeutil.getCurDateAndTime())
#
# #schedule.every(3).seconds.do(job)
# #schedule.every(10).minutes.do(job)
# #schedule.every().hour.do(job)
# schedule.every().day.at("05:59").do(job)
# #schedule.every(5).to(10).minutes.do(job)
# #schedule.every().monday.do(job)
# #schedule.every().wednesday.at("13:15").do(job)
# #schedule.every().minute.at(":17").do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
#     print(timeutil.getCurDateAndTime())
