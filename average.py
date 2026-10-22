num=[10,-5,20,-1,30,-8]
total=0
count=0
for i in num:
    if(i>=0):
        total+=i
        count+=1
average=total/count
print(average)