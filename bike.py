#vehicle type
vehicle=input("enter vehicle type: ")
#hours of renting
hrs=int(input("enter hrs of renting: "))
#helmet deposit
dep=input("is you want helmet deposit: ")
if(vehicle=="bike"):
    total=hrs*80
elif(vehicle=="scooter"):
    total=hrs*50
else:
    print("invalid input")
    exit()
if(dep=="yes"):
    total+=100
else:
    print("invalid input")
if(hrs>=5):
    total-=50
print("the total bill is=",total)
    
