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