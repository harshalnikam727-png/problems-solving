# #problem 1 safe division with input guard
# try:
#     a=int(input("enter numerator: "))
#     b=int(input("enter denominator: "))
#     result=a/b
#     print(f"division is {result}")
# except ZeroDivisionError:
#     print("cannot divisible by zero")
# except ValueError:
#     print("enter a valid integer")

# #problem 2 list item picker with safe exit
# def food(idx):
#     try:
        
#          print(f"you ordered {foods[idx]}")
#     except IndexError:
#         print("enter valid index")
#     except ValueError:
#         print("index should be integer")
#     finally:
#         print("thank you for visiting our store")

# foods=["pizza","burger","biryani","noodles","dosa"]
# print(foods)
# idx=int(input("enter the index of food item to order: "))
# food(idx)

# #problem 3 age & driving eligibility guard
# def eligibility():
#     raw_age=input("enter the age: ")
#     try:
#         age=int(raw_age)
#         if(age<0 or age>120):
#             raise ValueError ("age must be between 0 to 120")
#         if(age<18):
#             print("you are minor not alegible for license")
#         else:
#             print("eligible for license")
#     except ValueError as e:
#         print(f"invalid input {e}")
#     finally:
#         print("thank you for checking")
# eligibility()

# #problem 4 safe bank account withdrawal
# def value():
#     balance=5000
#     try:
#         amount=int(input("enter withdrawal amount: "))
#         if(amount<0 or amount>balance):
#             raise ValueError ("enter valid amount")
#         remaining=balance-amount
#         print(f"your remaining balance will be {remaining}")
#     except ValueError as e:
#         print(f"transaction failed {e}")
#     finally:
#         print("thank you for visiting")
# value()

# #problem 5 resiliant multi-data processor
# raw_records=[50,"20","invalid",0,10,"100","skip_me",25]
# processed=[]
# for ch in raw_records:
#     try:
#         val=int(ch)
#         result=1000//val
#         if result<20:
#             raise ValueError (f"result {result} is below minimum threshold (20)!")
#         processed.append(result)
#     except ZeroDivisionError:
#         print("skip message")
#     except ValueError as e:
#         print(f"skip message with {e}")
# print(processed)

#problem 6 safe food ordering & biling system
menu={"pizza":150,"burger":60,"biryani":120,"dosa":50}
print(menu)
def bill():
    total_bill=0
    while True:
        item=input("enter the item to order(or type done to exit): ").lower()
        if item=="done":
            break
        try:
            price=menu[item]
            qty=int(input("enter the quantity: "))
            if qty<=0:
                raise ValueError ("quantity must be at least 1")
            cost=price*qty
            total_bill+=cost
            print(f"added {qty} {item}(s)-rs{cost}")
        except KeyError:
            print(f"sorry,'{item}' is not found")
        except ValueError as e:
            print(f"invalid quantity {e}")
    print(f"your total bill is rs.{total_bill}")
    print("thank you for ordering")    

bill()

