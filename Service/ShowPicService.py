# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/13 上午 01:38
@Auth ： zhengxiong
@File ： ShowPicService.py
@QQ ：   2736590207
"""
import matplotlib.pyplot as plt  # plt显示图片
import matplotlib.image as mpimg  # mpimg读取图片
def showpicture(path):
    # 解决中文显示问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    img = mpimg.imread(path)
    # 此时的img已是一个数组
    var = img.shape  # 显示图片大小
    #print(var)
    plt.imshow(img)  # 显示图片
    plt.axis('on')  # 显示坐标轴
    plt.title('验证码')
    plt.show()
