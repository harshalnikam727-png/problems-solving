#train ticket pricing 
print("""base coach prices
"sleeper=400
"ac=1200
"meal=150""")
a=input("enter coach type(sleeper/ac): ")
b=input("do you want to add meal(yes/no): ")
if(a=="sleeper"):
    total=400
elif(a=="ac"):
    total=1200
else:
    print("invalid input")
    exit()
if(b=="yes" and a=="ac"):
    total+=150-50
elif(b=="yes"):
    total+=150
print("total bill is=",total)


