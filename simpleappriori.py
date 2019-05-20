
transactions=[]
minimum_confidence=70
items=set({})
C1=[]

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