
import itertools
import numpy as np

transactions=[]
minimum_confidence=70
items=set({})
C1=[]
min_sup=2
L=[]

def Support(itemset):
    count=0
    for transaction in transactions:
        if(set(itemset) <= set(transaction)):
            count=count+1
    return count


f= open("simpledata.txt", "r")
transactions_num=int(f.readline())
print(transactions_num)
for i in range(0,transactions_num):
    line=f.readline().split(' ')
    transactions.append([int(i) for i in line])
    items.update([ int(i) for i in line])

print(items)

for itm in items:
    C1.append([itm])

print(C1)
C=C1

i=1
while(i<3):
    print("Iter #"+str(i))
    C_temp=C
    for itemlst in C_temp:
        print(str(itemlst) + " : " + str(Support(itemlst)))
        if(Support(itemlst)<min_sup):
            C_temp.remove(itemlst)

    print(C_temp)
    L.append(C_temp)

    C=[]
    for itemlst_x in C_temp:
        for itemlst_y in C_temp:
            C.append(np.concatenate(itemlst_x,itemlst_x))

    #C=np.concatenate((C_temp,C_temp))
    i=i+1