#problem 1 running sum of a list
def running_sum(numbers):
    sum=0
    result=[]
    for i in numbers:
        sum+=i
        result.append(sum)
    return result
print(running_sum([1,2,3,4]))

#problem 2 categorise and count
scores=[82,35,67,90,41,28,75,53]
distinction=0
passed=0
failed=0
for i in scores:
    if(100>=i>=75):
        distinction+=1
    elif(75>i>=40):
        passed+=1
    elif(40>i>=0):
        failed+=1
    else:
        print("invalid input")
print("distinction=",distinction)
print("passed=",passed)
print("failed=",failed)
        
#problem 3 command dispatcher
actions=["add","view","edit","delete","export"]
for ch in actions:
    match (ch):
        case "add":
            print("Item added")
        case "delete":
            print("Item delete")
        case "view":
            print("Showing items")
        case _:
            print(f"invalid command:{ch}")

#problem 4 two pointer swap
items=[10,20,30,40,50]
left=0
right=len(items)-1
while left<right:
    items[left],items[right]=items[right],items[left]
    left+=1
    right-=1
print(items)

#problem 5 filter and transform(mixed condition)
data=[12,-4,"hello",7,0,"code",-9,15]
clean_data=[]
for i in data:
    if(isinstance(i,int)):
        if(i<0):
            continue
        elif(i%2==0):
            a=i/2
            clean_data.append(a)
        elif(i%2!=0):
            b=2*i
            clean_data.append(b)
    elif(isinstance(i,str)):
        c=i.upper()
        clean_data.append(c)
    else:
        print("invalid input")
print(clean_data)

#problem 6 frequency counter
items=["apple","banana","apple","orange","banana","apple"]
freq={}
apple=0
banana=0
orange=0
for ch in items:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

#problem 7 flatten a 2D matrix
matrix=[
    [1,2,3],
    [4,5],
    [6,7,8,9],
]
flat_list=[]
for i in matrix:
    for j in i:
        flat_list.append(j)
print(flat_list)

# problem 8 parse HTTP status codes & endpoints
logs=[
    ("get","/home",200),
    ("post","/login",200),
    ("get","/dashboard",404),
    ("delete","/user/10",500),
    ("put","/profile",403)
]
for i in logs:
    match (i):
        case(method,endpoint,status_code) if(status_code==200):
            print(f"{method} to {endpoint}")
        case (method,endpoint,status_code) if(status_code==404):
            print(f"not found:{endpoint} does not exist")
        case (method,endpoint,status_code) if(status_code==500):
            print(f"server error on {endpoint}")
        case(method,endpoint,status_code) :
            print(f"unhandeled status {status_code}")

#problem 9 paginate a list
data=[101,102,103,104,105,106,107,108]
page_size=3
pages=[]
for i in range(0,len(data),page_size):
    pages.append(data[i:i+page_size])
print(pages)