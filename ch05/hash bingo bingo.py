# -*- coding: utf-8 -*-
#lottery for binlog bingo
import requests
import re
import datetime
import time
import hashlib
from bs4 import BeautifulSoup


date_re = re.compile('[0-9]{2,3}/\d{1,2}/[0-9]{1,2}')
period_re = re.compile('\d{9}')

old_period = "" 
new_period = "" 

sec = int(input("更新秒數設定 : "))

while True:
    url = 'http://www.taiwanlottery.com.tw/'
    html = requests.get(url)
    html.encoding = 'utf-8'
    sp = BeautifulSoup(html.text ,'html.parser')
    gettime = datetime.datetime.now()
    
    lottery_num = sp.select(".ball_box01")
    lottery_guess = sp.select(".contents_mine_tx08")
    lottery_date = sp.select(".contents_mine_tx01")
    
    ##取得bingo bingo號碼
    lottery_num1 = lottery_num[0].find_all('div' ,{'class':'ball_tx'})
    lottery_guess1 = lottery_guess[0].find_all('div' ,{'class':'ball_red'})
    lottery_guess2 = lottery_guess[1].find_all('div' ,{'class':'ball_blue_BB1'})
    lottery_guess3 = lottery_guess[2].find_all('div' ,{'class':'ball_blue_BB2'})
    
    ##取得bingo bingo期數and時間
    lottery_date1 = lottery_date[0].find_all('span',{'class':'font_black15'})
    
    ##取得bingo bingo日期
    #lotterydate = date_re.findall(lottery_date1[0].text)[0]
    ##民國年份轉西元
    #lotteryyear = int(date_re.findall(lottery_date1[0].text)[0].split("/")[0] ) + 1911
    #date2ce = str(lotteryyear) + "/" + date_re.findall(lottery_date1[0].text)[0].split("/" ,1)[1]
    
    #print("bingo bingo時間 : " ,datetime.datetime.strptime(date2ce ,'%Y/%m/%d') )    
    
    new_period = period_re.findall(lottery_date1[0].text)[0]
    if hashlib.md5(old_period.encode("utf-8")).hexdigest() != hashlib.md5(new_period.encode("utf-8")).hexdigest():
        print("bingo bingo時間 : {}-{}-{} {}:{}:00".format(gettime.year ,gettime.month ,gettime.day ,gettime.hour ,gettime.minute - gettime.minute % 5) )
        old_period = period_re.findall(lottery_date1[0].text)[0]
        print("bingo bingo期數 : " ,period_re.findall(lottery_date1[0].text)[0] )
        
        for num in range(0 ,len(lottery_num1)):
            print(lottery_num1[num].text ,end = "\t")
    
        print() 
        
        print("超級獎號 : " ,lottery_guess1[0].text )
        print("猜大小 : " ,lottery_guess2[0].text )
        print("猜單雙 : " ,lottery_guess3[0].text )
        time.sleep(sec)
    else:
        print("資料尚未更新 ! {}秒後繼續檢查更新......" .format(sec))
        time.sleep(sec)



        
    
    
    