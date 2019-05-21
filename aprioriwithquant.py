from itertools import combinations

transactions=[]
minimum_confidence=70
items=set({})
C1=[]
min_sup=4
L=[]

def IsSubSet(S1,S2):
    for smaller in S1:
        is_smaller=False
        for bigger in S2:
            if CheckSameItemLessQuantity(smaller,bigger):
                is_smaller=True
                break
        if not is_smaller:
            return False
    return True

def CheckSameItemLessQuantity(s,b):

    sq = int(s.replace('(', '').replace(')', '').split(' ')[0])
    si = int(s.replace('(', '').replace(')', '').split(' ')[1])
    bq = int(b.replace('(', '').replace(')', '').split(' ')[0])
    bi = int(b.replace('(', '').replace(')', '').split(' ')[1])

    if (si == bi and sq <= bq):
        return True
    else:
        return False

def Subtract(first,second):
    return list(set(first) - set(second))


def Join(Cx,Cy):
    Cres=[]
    for lstx in Cx:
        for lsty in Cy:
            newlst=lstx + [x for x in lsty if x not in lstx]
            if(newlst not in Cx+Cy and sorted(newlst) not in Cres):
                Cres.append(sorted(newlst))
    for itemlst in Cres:
        for pair1 in itemlst:
            for pair2 in itemlst:
                sq = int(s.replace('(', '').replace(')', '').split(' ')[0])
                si = int(s.replace('(', '').replace(')', '').split(' ')[1])
                bq = int(b.replace('(', '').replace(')', '').split(' ')[0])
                bi = int(b.replace('(', '').replace(')', '').split(' ')[1])
    return Cres

def Support(itemset):
    count=0
    for transaction in transactions:
        if(IsSubSet(itemset,transaction)):
            count=count+1
    return count


f= open("data.txt", "r")
transactions_num=int(f.readline())
print(transactions_num)
for i in range(0,transactions_num):
    line=f.readline().replace('\n','').split(',')
    transactions.append([str(i) for i in line])
    items.update([ str(i) for i in line])

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
    if(len(itemlst)>=3):
        for k in range(1,len(itemlst)):
            allcomb=list(combinations(itemlst, k))
            for right in list(combinations(itemlst,k)):
                left=Subtract(itemlst,list(right))
                if(Support(itemlst)/Support(left)*100>minimum_confidence):
                    print(str(left)+" ----> "+ str(list(right)) + "   Confidence :" + str(100*Support(itemlst)/Support(left)))

