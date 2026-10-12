a=int(input("enter age: "))
if(0<a<=5):
    print("ticket price is free")
elif(5<a<=12):
    print("ticket price is 150 rupees")
elif(12<a<60):
    print("ticket price is 250 rupees")
elif(a>=60):
    print("ticket price is 180 rupees")
else:
    print("invalid age")
