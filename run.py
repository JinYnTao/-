# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:08:17 2018

@author: Administrator
"""
import os
pwd = os.getcwd()
os.chdir(pwd)
os.environ['NLS_LANG']='SIMPLIFIED CHINESE _ CHINA . UTF8 '
from MyPasture_V1001 import caigou
caigou=caigou()



if __name__ == '__main__':
    data,hms=caigou.welcome()
    up=input("是否更新采购记录？更新输入t，不更新请回车: ")
    if up=='t':
        data=caigou.update(data,hms)   
    else:
        pass
    data=caigou.nexts(data,hms)
    warn,warning,cgdata=caigou.warn(data,hms)
    print('#####################牧场采购预告######################')
    for xx in warn:
        print(xx)
    print('####################################################')
    print('  ')
    print('  ')
    print('*******************采购推迟警告**********************')
    for y in warning:
        print(y)
    print('****************************************************')
    





