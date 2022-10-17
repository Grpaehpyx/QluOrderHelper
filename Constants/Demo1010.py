# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/10 下午 11:04
@Auth ： zhengxiong
@File ： Demo1010.py
@QQ ：   2736590207
"""
def ini1():
    import entity.UserMoudle as userhander
    userhander._init()
    user=userhander.User(userid='123',mobile='33')
    userhander.set_user('key',user)

def ini2():
    import entity.UserMoudle as u
    print(u.get_value('key').userid)
    print(33)
ini1()
ini2()