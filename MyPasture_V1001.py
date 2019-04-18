# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 19:19:57 2018

@author: Administrator
"""
import pandas as pd
import datetime
import time
from DICT import WEEK_DAY_DICT

class caigou:
    def nexts(self,data,hms):
        for column in hms:
            x_max=[]
            column_next=column+'_next'
            data[column_next]=''
            for x in range(len(data)):
                if data[column][x]=='jyt' :
                    x_max.append(x)
            if len(x_max)>0:
                xmax=max(x_max)
                data[column_next][xmax+7]='jyt'
            else:
                pass
        return data
                    
    def findindex(self,data,date):
        for x in range(len(data)):
            if data['date'][x]==date:
                index_number=x
        return index_number
           
    def getBetweenDay(self,begin_date,end_date):
        
        date_list = []
        begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y-%m-%d")
            date_list.append(date_str)
            begin_date += datetime.timedelta(days=1)
        return date_list
    
    def get_week_day(self,date):
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        day = date.weekday()
        return WEEK_DAY_DICT[day]
    
    def welcome(self):
        print('***************************************************************************')
        print('**********************   欢迎使用JYT牧场记录    *************************')
        print('****************************************************************************')
        try:
            data=pd.read_Data('Data/mc.xlsx').fillna('')
            hms=pd.DataFrame(data.columns,columns=['hm']).applymap(lambda x:'' if 'next' in x or x=='weekday' or x=='date' else x)
            hms=list(hms[hms['hm']!='']['hm'])
        except:
            print('第一次使用引导')
            print('正在创建引导')
            print('Loading.........')
            data=pd.DataFrame([],columns=['date','weekday'])
            begin_date=str(datetime.datetime.now() + datetime.timedelta(days=-30))[0:10]
            end_date=str(datetime.datetime.now() + datetime.timedelta(days=+1000))[0:10]
            date_list=self.getBetweenDay(begin_date,end_date)
            data['date']=date_list.copy()
            data=data.fillna('')
            data['weekday']=data['date'].map(lambda x: self.get_week_day(x))
            time.sleep(1)
            hm='未知'
            hms=[]
            print('###################输入end结束创建###################')
            try:
                for x in range(0,200):
                    if hm=='end':
                        pass
                    else:
                        hm=''
                        hm = input("角色名称: ")
                        hm2 = hm+'_next'
                        data[hm]=''
                        data[hm2]=''
                        hms.append(hm)
                print('创建成功！')
            except:
                print('角色名称有误，创建失败')
            del data['end']
            del data['end_next']
            hms=hms[:-1]
            print('开始设置初始数据')
            print('---------------------------------------------------')
            for column in hms:
                print('现在正在进行'+column+'的历史记录创建')
                print("请输入"+column+"最近一次的(7天内)采购到访时间,今日输入today,其他日期格式如:2018-01-01")
                date = input("最近一次采购日期: ")
                if date=='today':
                    date=str(datetime.datetime.now())[:10]
                    index_number=self.findindex(data,date)
                    data[column][index_number]='jyt'
                    print('---------------------------------------------------')
                    continue
                elif date=='':
                    print(column+'无记录')
                    print('---------------------------------------------------')
                    continue
                else:
                    index_number=self.findindex(data,date)
                    data[column][index_number]='jyt'
                    print('---------------------------------------------------')
                    continue
            print('历史记录登记完成')
            data.to_excel('Data/mc.xlsx')
        data=pd.read_Data('Data/mc.xlsx').fillna('')
        return data,hms
    
    def update(self,data,hms):
        for column in hms:
            column_next=column+'_next'
            print('现在正在进行'+column+'的今日记录')
            date = input("请输入1进行记录: ")
            if date=='1':
                date=str(datetime.datetime.now())[:10]
                index_number=self.findindex(data,date)
                data[column][index_number]='jyt'
                data[column_next][index_number]=''
                print(''+column+'的今日记录已保存')
                print('具体内容为：'+date+' '+column+'的牧场来采购')
                print('---------------------------------------------------')
            elif date=='':
                print(column+'今日无记录')
                print('---------------------------------------------------')
                
                continue
        return data
        
    def warn(self,data,hms):
        date=str(datetime.datetime.now())[:10]
        index_number=self.findindex(data,date)
        warn=[]
        warn2=[]
        cgdata=[]
        for column in hms:
            column_next=column+'_next'
            for y in range(1,15):
                if data[column][index_number-y]=='jyt'and data[column][index_number]!='jyt':#如果第y天没来采购
                    if y<7:
                        data[column][:(index_number-y)]=data[column][:(index_number-y)].replace('jyt','jyt1')
                    else:
                        warn2.append(column+str(y)+'天没来，预计明天来采购')
                        data[column_next][:(index_number+1)]=''
                        data[column_next][index_number+1]='jyt'
                        pass
            for x in range(1,8):
                if data[column_next][index_number+x]=='jyt':
                    warn.append(column+'预计'+str(x)+'天后采购')
                    dat=pd.DataFrame([('','')],columns=['name','value'])
                    dat['name']=column
                    dat['value']=x
                    cgdata.append(dat)
        cgdata=pd.concat(cgdata,ignore_index=True)
        data.to_Data('Data/mc.xlsx')
        return warn,warn2,cgdata

    
    
    
    
    
    
    
    
    
    
    
    
    