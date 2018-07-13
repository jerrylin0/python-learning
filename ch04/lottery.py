# -*- coding: utf-8 -*-
#lottery
import requests
import re
import datetime
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
html.encoding = 'utf-8'
sp = BeautifulSoup(html.text ,'html.parser')

date_re = re.compile('[0-9]{2,3}/\d{1,2}/[0-9]{1,2}')
period_re = re.compile('\d{9}')

lottery_num = sp.select(".contents_box02")
lottery_date = sp.select(".contents_mine_tx02")

##取得威力彩號碼
lottery_num1 = lottery_num[0].find_all('div' ,{'class':'ball_tx'})
##取得威力彩期數and時間
lottery_date1 = lottery_date[0].find_all('span',{'class':'font_black15'})
##取得大樂彩號碼
lottery_num2 = lottery_num[2].find_all('div' ,{'class':'ball_tx'})
##取得大樂透期數and時間
lottery_date2 = lottery_date[2].find_all('span',{'class':'font_black15'})

##取得威力彩日期
lotterydate = date_re.findall(lottery_date1[0].text)[0]
##民國年份轉西元
lotteryyear = int(date_re.findall(lottery_date1[0].text)[0].split("/")[0] ) + 1911
date2ce = str(lotteryyear) + "/" + date_re.findall(lottery_date1[0].text)[0].split("/" ,1)[1]

print("威力彩時間 : " ,datetime.datetime.strptime(date2ce ,'%Y/%m/%d') )
print("威力彩期數 : " ,period_re.findall(lottery_date1[0].text)[0] )

for num in range(6 ,len(lottery_num1)):
    print(lottery_num1[num].text ,end = "\t")

print() 

##取得大樂透日期
lotterydate = date_re.findall(lottery_date2[0].text)[0]
##民國年份轉西元
lotteryyear = int(date_re.findall(lottery_date2[0].text)[0].split("/")[0] ) + 1911
date2ce = str(lotteryyear) + "/" + date_re.findall(lottery_date2[0].text)[0].split("/" ,1)[1]

print("大樂透時間 : " ,datetime.datetime.strptime(date2ce ,'%Y/%m/%d') )
print("大樂透期數 : " ,period_re.findall(lottery_date2[0].text)[0] )

for num in range(6 ,len(lottery_num2)):
    print(lottery_num2[num].text ,end = "\t")



