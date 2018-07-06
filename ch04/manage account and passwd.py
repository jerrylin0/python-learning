# -*- coding: utf-8 -*-
#manage the account and password
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

def read_data():
    with open ("c:/test/ttt.txt" ,'r' ,encoding = 'utf-8-sig') as f:
        filedata = f.read()
        if filedata != "":
            data = ast.literal_eval(filedata)
            return data
        else:
            return dict()

def disp_data():
    print("帳號\t密碼")
    print("=============")
    for key in data:
        print("{}\t{}" .format(key,data[key]))
    input("按任何鍵返回主選單!")

def input_data():
    while True:
        name = input("請輸入新增之帳號(按ENTER離開) :")
        if name == "":
            break
        if name in data:
            print("{}帳號已存在!" .format(name))
            continue
        passwd = input("請輸入新增帳號之密碼 :")
        data[name] = passwd
        with open("c:/test/ttt.txt" ,'w',encoding = 'utf-8-sig') as f:
            f.write(str(data))
        print("{}帳號已被儲存完畢!" .format(name))

def edit_data():
    while True:
        name = input("請輸入欲編輯之帳號(按ENTER離開) :")
        if name == "":
            break
        if name not in data:
            print("{}帳號不存在!" .format(name))
            continue
        print("原始密碼 :{}" .format(data[name]))
        passwd = input("請輸入新密碼 :")
        data[name] = passwd
        with open("c:/test/ttt.txt" ,'w',encoding = 'utf-8-sig') as f:
            f.write(str(data))
            print("密碼更改完畢，請按任意鍵返回主選單!")
            break

def delete_data():
    while True:
        name = input("請輸入欲刪除之帳號(按ENTER離開) :")
        if name == "":
            break
        if name not in data:
            print("{}帳號不存在!" .format(name))
            continue
        print("確定刪除{}之資料?" .format(data[name]))
        yn = input("(Y/N)?")
        if (yn == "Y" or yn == "y"):
            del data[name]
            with open("c:/test/ttt.txt" ,'w',encoding = 'utf-8-sig') as f:
                f.write(str(data))
                print("已刪除完畢，請按任意鍵返回主選單!")
                break        

import ast
import os

data = dict()
data = read_data()

#filepath = input("請輸入檔案位置 : ")
filepath = "c:/test/ttt.txt"


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

print("離開程式!")





        
    
    
    