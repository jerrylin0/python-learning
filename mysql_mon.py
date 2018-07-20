# -*- coding: utf-8 -*-
#user modify by mysql


def menu():
    os.system("cls")
    print("監控項目選擇：")
    print("----------------")
    print("1.Connection")
    print("2.Innodb row lock")
    print("0.結束程式")
    print("----------------")


def mysql_global_status():
    mysql_status_cursor = conn.cursor()
    mysql_status_cursor.execute("select json_objectagg(variable_name ,variable_value) \
                                from ( \
	                                    select variable_name ,variable_value \
	                                    from performance_schema.global_status \
	                                    union all \
	                                    select 'sys_time',now() \
	                                    ) x")
    mysql_status = json.loads(str(mysql_status_cursor.fetchone()[0])[2:-1])
    conn.commit()
    mysql_status_cursor.close()
    return mysql_status


def title_print(i_choice):
    i_opt = i_choice.split()
    title1 = "--------------------|"
    title2 = " time               |"

    while len(i_opt) != 0:
        if 'conn' in i_opt:
            title1 += "----------con----------|"
            title2 += " run   | conn  | mcon  |" # 6,6,6
            del i_opt[i_opt.index('conn')]
        elif 'lock' in i_opt:
            title1 += "------------wait-------------|"
            title2 += " waits   | waited  | wavg    |" # 8,8,8
            del i_opt[i_opt.index('lock')]

    print(title1)
    print(title2)


import mysql.connector
import json
import os
import time

##1.connection
threads_connected = 0
thread_running = 0

##2.innodb row lock

##0.global
title_cnt = 0
sys_time = 'N'
conn = mysql.connector.connect(user='dba', password='dba',host='10.101.60.80',database='jerry')

menu()
sec = int(input("請輸入監控間隔時間 :"))
choice = input("請輸入監控項目 :")


while True:
    mysql_status = mysql_global_status()
    if title_cnt == 10 or title_cnt == 0:
        title_print(choice)

    opt = choice.split()

    while len(opt) != 0:
        if sys_time == 'N':
            print("{:20s}" .format(mysql_status['sys_time']) ,end = '|')
            sys_time = 'Y'

        if 'conn' in opt:
            print(" {:6s}| {:6s}| {:6s}" .format(mysql_status['Threads_running'] , mysql_status['Threads_connected'] , mysql_status['Max_used_connections']) ,end='|')
            del opt[opt.index('conn')]
        elif 'lock' in opt:
            print(" {:8s}| {:8s}| {:8s}" .format(mysql_status['Innodb_row_lock_current_waits'],mysql_status['Innodb_row_lock_waits'],mysql_status['Innodb_row_lock_time_avg']) ,end='|')
            del opt[opt.index('lock')]

    print()
    title_cnt += 1
    sys_time = 'N'
    time.sleep(sec)

input("按任何鍵返回主選單!")

conn.close()
print("離開程式!")