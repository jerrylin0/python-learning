# -*- coding: utf-8 -*-
#ch04.py
import os
cur_path = os.path.dirname(__file__)
if (cur_path == ''):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    
print ("現在目錄 : " + cur_path)
print ("顯示__file__內容 : " + __file__)
#filename = os.path.abspath("ch04.py")
#filename = os.path.abspath("/home/mysql/ch04.py")
filename = os.path.abspath(__file__)

if (os.path.exists(filename)):
    print ("完整目錄(檔案)名稱 : " + filename)
    
    print ("是否為目錄 ? " + str(os.path.isdir(filename)))
    
    basename = os.path.basename(filename)
    print ("目錄或檔案名稱 : " + basename)
    
    if (os.path.isfile(filename) == True):
        dirname = os.path.dirname(filename)
        print ("檔案路徑 : " + dirname)
    
        print ("檔案大小 : " + str(os.path.getsize(filename)))
        
        fullpath ,fname = os.path.split(filename)
        print ("目錄路徑 : " + fullpath)
        print ("檔案名稱 : " + fname)
        
        drive,fpath = os.path.splitdrive(filename)
        print ("硬碟機(only for windowns ,on linux is null) : " + drive)
        print ("路徑名稱 : " + fpath)
        
        print ("組合路徑 : " + os.path.join(fullpath + "/" + fname))

# -*- coding: utf-8 -*-
#ch04.py
import os
cur_path = os.path.dirname(__file__)
if (cur_path == ''):
    cur_path = os.path.dirname(os.path.abspath(__file__))
    
sample_tree = os.walk(cur_path)

for dirname ,subdir ,files in sample_tree:
    print ("檔案路徑 : " + str(dirname))
    print ("目錄串列 : " + str(subdir))
    print ("檔案串列 : " + str(files))
    print ("")

# -*- coding: utf-8 -*-
#ch04.py
import glob
files1 = glob.glob("*.py")
files2 = glob.glob("*.txt")
print(files1 + files2)



	

