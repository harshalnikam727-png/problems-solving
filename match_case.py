# problem 1 http status code decoder
https_status=int(input("enter http status code: "))
match https_status:
    case 200:
        print("ok")
    case 400:
        print("bad request")
    case 404:
        print("not found")
    case 500:
        print("internal service error")
    case _:
        print("unknown code")

# problem 2 day of the week
day=int(input("enter day number: "))
match day:
    case _ if(0<day<=5):
        print("weekdays")
    case _ if(5<day<=7):
        print("weekend")
    case _:
        print("invalid input")

# problem 3 2d/3d coordinate identifier
point=(3,6,8)
match point:
    case (0,0):
        print("origin")
    case (x,0):
        print(f"the point is on the x-axis on {x}")
    case (0,y):
            print(f"the point is on the y-axis on {y}")
    case (x,y):
            print(f"the point is 2d on ({x},{y})")
    case (x,y,z):
            print(f"the point is 3d on ({x},{y},{z})")
        
# problem 4 CLI command parser
command=["move","old.py","new.py"]
match command:
    case ["quit"] | ["exit"]:
        print("exiting application...")
    case ["save",filename]:
        print(f"saving data to {filename} ")
    case ["move",src,dest]:
        print(f"moving file from {src} to {dest}")
    case _:
        print("unknown command format")
    
   
# problem 5 quadrant dictator
point=(0,9)
match point:
    case (0,0):
        print("origin")
    case (x,y)  if(x>0 and y>0):
        print(f"({x},{y}) is in 1st quadrant")
    case (x,y)  if(x<0 and y>0):
         print(f"({x},{y}) is in 2nd quadrant")
    case (x,y)  if(x<0 and y<0):
        print(f"({x},{y}) is in 3rd quadrant")
    case (x,y)  if(x>0 and y<0):
        print(f"({x},{y}) is in 4th quadrant")
    case (x,y)  if(x==0 or y==0):
            print(f"({x},{y}) is on axis")
        
    case _ :
        print("invalid input")

# problem 6 E-commerce order discount calender
order=("laptop",3,45000)
match order:
    case(item,quantity,price) if(quantity>=5):
        bill=quantity*price*0.9
        print(f"{quantity} {item}'s bill is {bill}")
    case(item,quantity,price) if(1<=quantity<5):
        bill=quantity*price
        print(f"{quantity} {item}'s bill is {bill}")
    case(item,quantity,price) if(quantity<0):
        print(f"invalid order format")
    case _:
        print("invalid order")
      
