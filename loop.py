#challenge 1
l1=["a","Avacado","banana","Avacado","cherry","apricot","mango"]
count=0
for w in l1:
    if(w[0]=="a" or w[0]=="A"):
       count+=1
print("total words starting with a or A is:",count)

# challenge 2 finding long words
words=["python","code","programming","ai","loop","developer"]
count=0
for w in words:
    if(len(w)>5):
        count+=1
print(count)

# challenge 3 the collector pattern
num=[12,7,19,24,30,5,8]
even=[]
for i in num:
    if(i%2==0):
        even.append(i)
print(even)

# challenge 4 remove duplicates
num=[4,2,7,4,9,2,8,4]
unique_num=[]
for i in num:
    if i  not in unique_num:
        unique_num.append(i)
print(unique_num)

# challenge 5 reverse a string
text="python"
rev=""
for c in text:
    rev=c+rev
print(rev)

# challenge 6 running sum of an array
num=[9,7,4,8]
total=0
running_sum=[]
for i in num:
    total+=i
    running_sum.append(total)
print(running_sum)

# challenge 7 replace with maximum seen so far
num=[3,1,4,1,5,9,2,6]
high=num[0]
result=[]
for i in range(0,len(num)):
    if(num[i]>=high):
        high=num[i]
    result.append(high)
print(result)

