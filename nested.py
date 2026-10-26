# challenge 1 the multiplication table
for i in range(1,4):
    for j in range(1,5):
        print(i,"x",j,"=",i*j)

# challenge 2 combine 2 list
colors=["red","blue"]
sizes=["s","m","l"]
for i in colors:
    for j in sizes:
        print(i,"-",j)

# challenge 3 find common elements
st1=[1,5,10,20,40,80]
st2=[6,7,20,80,100]
common=[]
for x in st1:
    for y in st2:
        if(x==y):
            common.append(x)
print(common)

# challenge 4 count numbers smaller than current
nums=[8,1,2,2,3]
result=[]
for i in nums:
    count=0
    for j in nums:
        if(j<i):
            count+=1
    result.append(count)
print(result)

# challenge 5 find unique pairs that sum to a target
nums=[2,4,3,5,7,8,9]
target=7
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j]==target):
            print("pair found=",nums[i],nums[j])

# challenge 6 contains duplicate
num=[1,2,3,4]
has_duplicate="false"
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]==num[j]):
            has_duplicate="true"
            break
print(has_duplicate)

# challenge 7 sum of each row in a 2d grid
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
for i in matrix:
    row_sum=0
    for j in i:
        row_sum+=j
    print(row_sum)

