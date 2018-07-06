# -*- coding: utf-8 -*-
list=[]
for i in range(1 ,10):
    list.append([])
    for j in range(1 ,10):
        list[i-1].append(i*j)
        print ('%d*%d = %-2d   '%(j ,i ,list[i-1][j-1] ) ,end='')
    print ('')

# -*- coding: utf-8 -*-
for i in range(1,10):
	for j in range(1,10):
		print ('%d*%d = %-2d ' %(j,i,i*j) ,end = '')
	print ()

# -*- coding: utf-8 -*-
#prime
n = input("please enter a number that more than two :")
n = int(n)
if (n >= 2):
    if (n==2):
        print ("this number %d is a prime number!" %n)
    else:
        for i in range(2,n):
            if (n % i == 0):
                print ("this number {} not a prime number!!" .format(n) )
                break
        else:
            print ("this number %d is a prime number!!!" %n)
else:
    print ('your enter this number {} that is less than two' .format(n))

# -*- coding: utf-8 -*-
#score
score = 0
total = 0
person = 0
while (score >=0):
    person += 1
    total += score
    score = input("please enter the score of student {} :" .format(person))
    score = float(score)
print ("this class has %d students ,the total score is %-7.2f , the average score is %5.2f" %(person - 1 ,total ,total/(person - 1)))

# -*- coding: utf-8 -*-
#score
score = 0
total = 0
score_list = []
while (score >=0):
    score = input("please enter the student score :")
    score = float(score)
    score_list.append(score)

for i in range(0 ,len(score_list) - 1):
    total += score_list[i]
    
print ("this class has %d students ,the total score is %-7.2f , the average score is %5.2f" %(len(score_list) - 1 ,total ,total/(len(score_list) - 1)))

# -*- coding: utf-8 -*-
#func
inlist = []
num = 0
while (num >= 0):
    num = int(input("please enter a number :"))
    inlist.append(num)
inlist.pop()
print ("the max:%2d  ,the min:%2d  ,the sum:%2d" %(max(inlist) ,min(inlist) ,sum(inlist)) )
print ("{}  or  {}" .format( sorted(inlist) ,sorted(inlist ,reverse=True)))









