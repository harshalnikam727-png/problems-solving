#problem 1 word length dictionary
# s=input("enter the sentence: ")
# a=s.split()
# dic={}
# for ch in a:
#     dic[ch]=len(ch)
# print(dic)

#problem 2 student marks lookup
# marks={
#     "harry":92,
#     "rohan":76,
#     "aakash":85,
#     "priya":90,
# }
# a=input("enter the students name: ")
# b=marks.get(a)
# if b is None:
#     print("student not found")
# else:
#     print(f"marks of student is:{b}")

#problem 3 character frequency counter
# s=input("enter the character: ")
# freq={}
# for ch in s:
#     if(ch in freq):
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# for key,values in freq.items():
#     print(f"{key}:{values}")

#problem 4 update invetory
# stock={
#     "apples":10,
#     "bananas":5,
#     "oranges":8,
# }
# item=input("enter the fruit name: ")
# qty=int(input("enter the new quantity of fruit: "))
# stock.update({item:qty})
# print(stock)

#problem 5 remove an item using .pop()
# prices={
#     "pen":10,
#     "notebook":50,
#     "eraser":5,
#     "ruler":15,
# }
# item1=input("enter item to be removed: ")
# removed_price=prices.pop(item1)
# print(f"removed {item1} with price:{removed_price}")
# item2=input("enter the item to be added: ")
# pr=int(input("enter the price of item to be added: "))
# prices.update({item2:pr})
# print(f"{item2} with price {pr} is added")
# print(prices)

#problem 6 pass/fail classifier
# scores={
#     "alice":85,
#     "bob":38,
#     "charlie":62,
#     "daisy":31,
#     "ethan":74
# }
# passed={}
# failed={}
# for key,values in scores.items():
#     if(values<40):
#         failed.update({key:values})
#     elif(values>=40):
#         passed.update({key:values})
#     else:
#         print("invalid input")
# print("passed:", passed)
# print("failed:", failed)

#problem 7 total bill calculator
# menu={
#     "pizza":150,
#     "burger":60,
#     "fries":50,
#     "coke":30
# }
# total=0
# n=int(input("how many items: "))
# for i in range(n):
#     item=input("enter item name: ")
#     qty=int(input("enter the quantity: "))
#     if item in menu:
#         total+=menu[item]*qty
#     else:
#         print(f"{item} is not in menu ")
# print(f"the total bill is :{total}")

#problem 8 even/odd number grouper
# classified={
#     "even":[],
#     "odd":[],
# }
# s=input("enter numbers separated by space: ")
# l=s.split()
# for i in l:
#     num=int(i)
#     if(num%2==0):
#         classified["even"].append(num)
#     else:
#         classified["odd"].append(num)
# print(classified)

#problem 9 vowel counter 
# vowels={"a":0,"e":0,"i":0,"o":0,"u":0}
# text=input("enter a sentence: ")
# text=text.lower()
# for ch in text:
#     if ch in vowels:
#         vowels[ch]+=1
# for k,v in vowels.items():
#     if(v>0):
#         print(f"{k}:{v}")

#problem 10 phone directory
# phone_book={
#     "harry":"9876543210",
#     "rohan":"9123456780"
# }
# while True:
#     print("1.search contact")
#     print("2.add contact")
#     print("3.exit")
#     choice=int(input("enter choice(1/2/3): "))
#     if(choice==1):
#         name1=input("enter the name to search: ").lower()
#         if name1 in phone_book:
#             print(phone_book[name1])
#         else:
#             print("contact not found")
#     elif(choice==2):
#         name2=input("enter name: ").lower()
#         number=input("enter the phone number: ")
#         phone_book.update({name2:number})
#         print(f"contact {name2} saved succesfully")

#     elif(choice==3):
#         print("thank you")
#         break
#     else:
#         print("invalid choice")
    
#problem 11 final boss challenge 
#students grade tracker
students={}
while True:
    print("1.add student")
    print("2.display class summary")
    print("3.remove students")
    print("4.exit")
    choice=int(input("enter the choice(1/2/3/4): "))
    if(choice==1):
        name1=input("enter the student name: ")
        marks=int(input("add their marks(0-100): "))
        students[name1]=marks
    elif(choice==2):
        student=0
        mark=0
        highest=0
        for k,v in students.items():
            student+=1
            mark+=v
            if(v>highest):
                highest=v
                topper=k
        avg=mark/student
        print(f"average mark is: ",avg)
        print(f"topper is {topper} with marks {highest} ")
    elif(choice==3):
        name2=input("enter the name of student to be removed: ")
        students.pop(name2)
        print(f"{name2} removed succesfully")
    elif(choice==4):
        print("thank you")
        break
    else:
        print("invalid input")
        
