import QueryEmpty
import Service.CaptchaService as capService
import Service.FristQuery as firstQuery
import Service.LoginService as loginService
import Service.OrderService as orderService
import Service.CookieHandler as cookieHandler
import entity.UserMoudle as userhander
import entity.ParamAndConfig as config

cookies=firstQuery.getCookies()
capService.setcook('PHPSESSID='+config.get_value('firstqueryid'))
capService.getCaptchaAndSave()

loginService.setcookie('PHPSESSID='+config.get_value('firstqueryid'))

verify=int(input("请输入验证码\n"))
print("登入ing=========================")
print("您可将本系统看作您的另一台设备,如果账号已经处于登入状态,再次登入时会将别的设备的账号挤下去")
loginService.login('201911010012','qlu162315',verify)
#
# print("根据条件查询位置状况")
# QueryEmpty.getDetailsByCondition()
#
# print("预约ing============")
# orderService.setcookie(str)
#
# pool=userMoudle.get_global_pool()['201911010012']
# print(userMoudle.get_global_pool())
# print(pool)
# tokenstr='access_token='+pool['data']['_hash_']['access_token']
# token=pool['data']['_hash_']['access_token']
# expire='expire='+pool['data']['_hash_']['expire']
# print(tokenstr)
# print(expire)
# orderService.settoken(token)
# orderService.setcookie(tokenstr)
# orderService.setcookie(expire)
# curcook=orderService.getcookie()
# print(curcook)
# orderService.order()