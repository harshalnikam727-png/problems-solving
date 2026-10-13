#popcorn size
size=input("enter pop corn size: ")
#wants drink 
drink=input("is you want drink or not: ")
s=120
m=180
l=240
d=60
if(size=="small"):
    if(drink=="true"):
        print("the price is:",s+d)
    else:
        print("price is:",s)
elif(size=="medium"):
    if(drink=="true"):
            print("the price is:",m+d)
    else:
            print("price is:",m)
elif(size=="large"):
     if(drink=="true"):
             print("the price is:",l+d-30)
     else:
             print("price is:",l)
else:
      print("invalid input")