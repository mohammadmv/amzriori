
import itertools
import numpy as np

transactions=[]
minimum_confidence=70
items=set({})
C1=[]
min_sup=2
L=[]


def divide(iterable, parts):
    ''' Partitions an iterable into parts number of lists. '''
    items = list(iterable)

    seqs = [[] for _ in range(parts)]
    while items:
        for i in range(parts):
            if not items:
                break

            seqs[i].append(items.pop())

    return seqs

def Subtract(lst,itm):
    return list(set(lst) - set([itm]))

def Join(Cx,Cy):
    Cres=[]
    for lstx in Cx:
        for lsty in Cy:
            newlst=lstx + [x for x in lsty if x not in lstx]
            if(newlst not in Cx+Cy and sorted(newlst) not in Cres):
                Cres.append(sorted(newlst))

    return Cres

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
while(True):
    print("Iter #"+str(i))
    C_temp=[]
    for itemlst in C:
        if(Support(itemlst)>=min_sup):
            print(str(itemlst) + " : " + str(Support(itemlst)))
            C_temp.append(itemlst)

    #print(C_temp)
    L=L+C_temp

    C=[]
    #for itemlst_x in C_temp:
    #    for itemlst_y in C_temp:
    #        C.append(np.concatenate(itemlst_x,itemlst_x))

    C=Join(C_temp,C_temp)
    if(len(C)==0):
        print("Finish")
        break;
    i=i+1

print("L:")
print(L)



for itemlst in L:
    allperms=[itemlst[i::2] for i in range(2)]
    print(divide(itemlst,2))
    if(len(itemlst)>=3):
        for item in itemlst:
            print(str(Subtract(itemlst,item))+" ----> "+ str(item) + "   Confidence :" + str(Support(itemlst)/Support(Subtract(itemlst,item))))

