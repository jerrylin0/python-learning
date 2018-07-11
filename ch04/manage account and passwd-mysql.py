# -*- coding: utf-8 -*-
#user modify by mysql
def menu():
    os.system("cls")
    print("帳號/密碼管理系統")
    print("----------------")
    print("1.新增帳號/密碼")
    print("2.顯示帳號/密碼")
    print("3.修改帳密碼")
    print("4.刪除帳號/密碼")
    print("0.結束程式")
    print("----------------")

def disp_data():
    
    cursor = conn.cursor()
    cursor.execute("select name ,passwd from user")
    
    print("帳號\t密碼")
    print("=============")
    for (name ,passwd) in cursor :
        print("{}\t{}" .format(name,passwd) )
    
    
    conn.commit()
    cursor.close()
    input("按任何鍵返回主選單!")

def input_data():     
    while True:
        name = input("請輸入新增之帳號(按ENTER離開) :")
        if name == "":
            break
        
        query = ("select name ,passwd from user where name = '{}';" .format(name))
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        if not row==None:
            print("{}帳號已存在!" .format(name))
            continue
        
        passwd = input("請輸入新增帳號之密碼 :")
        query = ("insert into user(name,passwd) values('{}','{}') ;".format(name ,passwd))

        cursor.execute(query)
        conn.commit()
        cursor.close()
        print("{}帳號已被儲存完畢!" .format(name))

def edit_data():
    while True:
        name = input("請輸入欲編輯之帳號(按ENTER離開) :")
        if name == "":
            break
        
        row = check_data(name)
        if row == None:
            print("{}帳號不存在!" .format(name))
            continue
        
        print("原始密碼 :{}" .format(row[1]))
        passwd = input("請輸入新密碼 :")
        
        query = ("update user set passwd = '{}' where name = '{}';" .format(passwd ,name))

        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        print("密碼更改完畢，請按任意鍵返回主選單!")
        break

def delete_data():
    while True:
        name = input("請輸入欲刪除之帳號(按ENTER離開) :")
        if name == "":
            break
        
        row = check_data(name)
        if row == None:
            print("{}帳號不存在!" .format(name))
            continue
            
        print("確定刪除{}之資料?" .format(row[0]))
        yn = input("(Y/N)?")
        if (yn == "Y" or yn == "y"):
            query = ("delete from user where name = '{}'" .format(name))
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
            print("已刪除完畢，請按任意鍵返回主選單!")
            break        

def check_data(name):
    query = ("select name ,passwd from user where name = '{}' ;" .format(name))
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    return row
    
import os
import mysql.connector

conn = mysql.connector.connect(user='dba', password='dba',host='10.101.60.80',database='jerry')

while True :
    menu()
    choice = int(input("請輸入您得選擇 : "))
    print()
    if choice == 1:
        input_data()
    elif choice == 2:
        disp_data()
    elif choice == 3:
        edit_data()
    elif choice == 4:
        delete_data()
    else:
        break
conn.close()
print("離開程式!")


        
    
    
    