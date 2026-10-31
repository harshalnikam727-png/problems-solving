#problem 1 temperature converter
def celcius_to_farhenhite(celcius):
    farhenhite=(celcius*9/5)+32
    print(f"celcius to farhenhite is {farhenhite}")
    return
celcius=float(input("enter celcius temp.: "))
celcius_to_farhenhite(celcius) 

#problem 2 number sign & parity checker
def analyze(n):
    if(n>0 and n%2==0):
        return "positive even"
    elif(n>0 and n%2!=0):
       return"positive odd"
    elif(n<0 and n%2==0):
        return"negative even"
    elif(n<0 and n%2!=0):
        return"nagative odd"
n=int(input("enter any number: "))
print(analyze(n))

#problem 3 bill spitter with tip 
def calculate_bill(amount,tip_percent,split_by):
    tip=amount*(tip_percent/100)
    total=amount+tip
    per_person=total/split_by
    return per_person
a=int(input("enter bill amount to be split: "))
b=int(input("enter tip percentage: "))
c=int(input("enter in how many parts to be split: "))
print(calculate_bill(a,b,c))

#problem 4 strong password validator
def is_strong_password(password):
    if(len(password)<8 ):
        return False
    
    has_uppercase=False
    has_lowercase=False
    has_digit=False

    for ch in password:
        if(ch.isupper()):
            has_uppercase=True
        elif(ch.islower()):
            has_lowercase=True
        elif(ch.isdigit()):
            has_digit=True

    return has_digit and has_lowercase and has_uppercase 
a=input("enter password: ")
print(is_strong_password(a))

#problem 5 custom multi-number statistics
def calculate_stats(*numbers):
    if(len(numbers)==0):
        return None

    total=0
    count=0
    max=0
    for i in numbers:
        total=total+i
        count=count+1
        if(i>max):
            max=i
    average=total/count
        
    return total , count ,average , max

print(calculate_stats(2,45,65,7))

#problem 6 build a user profile
def build_profile(username,**details):
    print(f"user:{username}")
    for key ,value in details.items():
        print(f"-{key.capitalize()}:{value}")
    return len(details)

print(build_profile("alex_dev",role="backend developer",city="pune",status="active"))

#problem 7 flexible order biling system
def invoice(customer_name,*prices,**discounts):
    subtotal=0
    for i in prices:
        subtotal+=i

    total_discounts=0
    for value in discounts.values():
        total_discounts+=value
        if(total_discounts>50):
            total_discounts=50

    final_amount=subtotal*(1-(total_discounts/100))
    return(subtotal,final_amount)

print(invoice("priya",1000,flat=40,member=20))

#problem 8 the multi-score evaluator
def scores(passing_score=40,*scores):
    passed_count=0
    failed_count=0
    sum=0
    for values in scores:
        if(values>=passing_score):
            passed_count+=1
        elif(values<passing_score):
            failed_count+=1
        else:
            return 0,0,0.0
        sum+=values
    average=sum/(passed_count+failed_count)
    return passed_count,failed_count,average
print(scores(40,55,32,78,90,20))


#problem 9 the flexible shopping cart
def cart(tax_rate=0.05,*prices,**coupons):
    if(len(prices)==0):
        return 0.0,0.0
    subtotal=0
    for i in prices:
        subtotal+=i
    coupon=0
    for key,value in coupons.items():
        coupon+=value
    discounted_price=subtotal-coupon
    if(discounted_price<0):
        discounted_price=0
    tax=discounted_price*tax_rate
    final_total=discounted_price+tax
    return subtotal,round(final_total,2)
print(cart(0.05,500,300,200,welcome=50))

        
#problem 10 the final boss
def student_report(passing_grade=40,*marks,**extra_credits):
    if(len(marks)==0):
        return 0
    marks_sum=0
    for i in marks:
        marks_sum+=i
    extra_credit=0
    for key,value in extra_credits.items():
        extra_credit+=value
    final_score=marks_sum+extra_credit
    if(final_score>100*len(marks)):
        final_score=100*len(marks)
    percentage=final_score/len(marks)
    if(percentage>=passing_grade):
        status="Pass"
    else:
        status="Fail"
    return round(final_score,2),status,len(marks)
print(student_report(40,50,60,70,sports=5,debate=3))

#problem 11 GYM membership fee calculator
def gym(base_fee=1000,*services,**extra_charges):
    total_services=0
    for i in services:
        total_services+=i
    total_extra=0
    for key,value in extra_charges.items():
        total_extra+=value
    gross_total=base_fee+total_extra+total_services
    if(gross_total>=3000):
        discount=0.1*gross_total
    else:
        discount=0
    net_fee=gross_total-discount
    return gross_total,round(net_fee,2)
print(gym(1000,500,300,trainer=1500))

#problem 12 freelance invoice generator
def bill(hourly_rate=500,*hours_worked,**bonus_fee):
    total_hours=0
    for i in hours_worked:
        total_hours+=i
    base_pay=total_hours*hourly_rate
    total_bonus=0
    for value in bonus_fee.values():
        total_bonus+=value
    gross_pay=base_pay+total_bonus
    if(gross_pay>=5000):
        platform_fee=0.05*gross_pay
    else:
        platform_fee=0
    net_payment=gross_pay-platform_fee
    return total_hours,gross_pay,round(net_payment,2)
print(bill(400,2,3,tip=200))