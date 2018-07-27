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


def get_mysql_global_status():
    mysql_global_status_cursor = conn.cursor()
    mysql_global_status_cursor.execute("show global status")
    mysql_global_status = mysql_global_status_cursor.fetchall()

    '''
    mysql_status_cursor.execute("select json_objectagg(variable_name ,variable_value) \
                                from ( \
                                        select variable_name ,variable_value \
                                        from performance_schema.global_status \
                                        union all \
                                        select 'sys_time',now() \
                                        ) x")
    mysql_status = json.loads(str(mysql_status_cursor.fetchone()[0])[2:-1])
    '''
    #conn.commit()
    mysql_global_status_cursor.close()
    return dict(mysql_global_status)


def get_title(i_choice):
    i_opt = i_choice.split()
    title1 = "--------|"
    title2 = "    time|"

    while len(i_opt) != 0:
        if 'thread' in i_opt:
            title1 += "-------thread-------|"
            title2 += "  run  con  cac  cre|"
            del i_opt[i_opt.index('thread')]
        elif 'lock' in i_opt:
            title1 += "--lock wait----|"
            title2 += "   cu   wa   ti|"
            del i_opt[i_opt.index('lock')]
        elif 'mysql' in i_opt:
            title1 += "------TPS/QPS-------|----com/roll---|"
            title2 += "    i    u    d    s|    c    r   rh|"
            del i_opt[i_opt.index('mysql')]
        else:
            return '-1'
    return title1 + '\n' + title2


import mysql.connector
import os
import time
import datetime

##1.connection
threads_connected = 0
thread_running = 0

##2.innodb row lock

##3.mysql status
##TPS/QPS
old_insert = -1
old_update = -1
old_delete = -1
old_select = -1
old_commit = -1
old_rollback = -1

##thread
old_thread_created = -1

##row lock
old_row_lock = -1

##0.global
title_cnt = -1
sys_time = 'N'
conn = mysql.connector.connect(user='dba', password='dba', host='10.101.60.80', database='jerry', autocommit=True)

menu()
sec = int(input("請輸入監控間隔時間 :"))

while True:
    choice = input("請輸入監控項目 :")
    while True:
        if title_cnt == 15 or title_cnt == -1:
            title_return = get_title(choice)
            if title_return == '-1':
                print("監控項目有誤，請重新輸入監控項目...")
                break
            print(title_return)
            title_cnt = 0

        mysql_status = get_mysql_global_status()
        opt = choice.split()

        while len(opt) != 0:
            if sys_time == 'N':
                print("{:8s}" .format(datetime.datetime.now().strftime('%H:%M:%S')), end='|')
                sys_time = 'Y'

            if 'thread' in opt:
                if old_thread_created == -1:
                    diff_thread_created = 0
                    old_thread_created = int(mysql_status['Threads_created'])
                else:
                    diff_thread_created = int(mysql_status['Threads_created']) - old_thread_created
                    old_thread_created = int(mysql_status['Threads_created'])

                print("{:5d}{:5d}{:5d}{:5d}" .format(int(mysql_status['Threads_running']), int(mysql_status['Threads_connected']), int(mysql_status['Threads_cached']), diff_thread_created), end='|')
                del opt[opt.index('thread')]
            elif 'lock' in opt:
                if old_row_lock == -1:
                    diff_row_lock = 0
                    old_row_lock = int(mysql_status['Innodb_row_lock_waits'])
                else:
                    diff_row_lock = int(mysql_status['Innodb_row_lock_waits']) - old_row_lock
                    old_row_lock = int(mysql_status['Innodb_row_lock_waits'])

                print("{:5d}{:5d}{:5.2f}" .format(int(mysql_status['Innodb_row_lock_current_waits']), diff_row_lock, int(mysql_status['Innodb_row_lock_time'])/1000), end='|')
                del opt[opt.index('lock')]
            elif 'mysql' in opt:
                if old_insert == -1:
                    diff_insert = 0
                    old_insert = int(mysql_status['Com_insert']) + int(mysql_status['Com_insert_select'])
                else:
                    diff_insert = int(mysql_status['Com_insert']) + int(mysql_status['Com_insert_select']) - old_insert
                    old_insert = int(mysql_status['Com_insert']) + int(mysql_status['Com_insert_select'])

                if old_update == -1:
                    diff_update = 0
                    old_update = int(mysql_status['Com_update']) + int(mysql_status['Com_update_multi'])
                else:
                    diff_update = int(mysql_status['Com_update']) + int(mysql_status['Com_update_multi']) - old_update
                    old_update = int(mysql_status['Com_update']) + int(mysql_status['Com_update_multi'])

                if old_delete == -1:
                    diff_delete = 0
                    old_delete = int(mysql_status['Com_delete']) + int(mysql_status['Com_delete_multi'])
                else:
                    diff_delete = int(mysql_status['Com_delete']) + int(mysql_status['Com_delete_multi']) - old_delete
                    old_delete = int(mysql_status['Com_delete']) + int(mysql_status['Com_delete_multi'])

                if old_select == -1:
                    diff_select = 0
                    old_select = int(mysql_status['Com_select'])
                else:
                    diff_select = int(mysql_status['Com_select']) - old_select
                    old_select = int(mysql_status['Com_select'])

                if old_commit == -1:
                    diff_commit = 0
                    old_commit = int(mysql_status['Com_commit'])
                else:
                    diff_commit = int(mysql_status['Com_commit']) - old_commit
                    old_commit = int(mysql_status['Com_commit'])

                if old_rollback == -1:
                    diff_rollback = 0
                    old_rollback = int(mysql_status['Com_rollback']) + int(mysql_status['Com_rollback_to_savepoint'])
                else:
                    diff_rollback = int(mysql_status['Com_rollback']) + int(mysql_status['Com_rollback_to_savepoint']) - old_rollback
                    old_rollback = int(mysql_status['Com_rollback']) + int(mysql_status['Com_rollback_to_savepoint'])

                print("{:5d}{:5d}{:5d}{:5d}|{:5d}{:5d}{:5.2f}" .format(diff_insert, diff_update, diff_delete, diff_select
                                                                       , diff_commit ,diff_rollback
                                                                       , (int(mysql_status['Com_rollback']) + int(mysql_status['Com_rollback_to_savepoint']))
                                                                       / (int(mysql_status['Com_commit']) + int(mysql_status['Com_rollback']) + int(mysql_status['Com_rollback_to_savepoint']))), end='|')
                del opt[opt.index('mysql')]

        print()
        title_cnt += 1
        sys_time = 'N'
        time.sleep(sec)



input("按任何鍵返回主選單!")

conn.close()
print("離開程式!")