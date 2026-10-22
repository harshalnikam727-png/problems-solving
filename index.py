num=[40,10,25,80,55]
target=25
found=False
for i in range(len(num)):
    if(num[i]==target):
        print("the index of targeted no. is:",i)
        break
    else:
        print("no index found")
