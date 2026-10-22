n=int(input("enter any number: "))
for i in range(1,11):
    if(i%4==0):
        continue
    else:
        print(n*i)
