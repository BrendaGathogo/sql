#if statement
x=5
marks=43
grade=5
if(x>0):
    print("The number is positive")
#if...else statement
if(marks>=50):
    print("You have passed the exam")
else:
    print("You have failed the exam")
#if...elif...else statement
if(grade<=29 and grade>=0):
    print("You failed")
elif(grade>=30 and grade<=49):
    print("You have passed")
elif grade>=50 and grade<=79:
    print("You have a credit")
elif grade>=80 and grade<=100:
    print("You have a distinction")
else:
    print("Wrong grade entered")
#Example1
order="chapati"
if order=="chapati":
    print("cost of order is KSH.30")
elif order=="pilau":
    print("cost of order is KSH.150")
elif order=="samosa":
    print("cost of order is KSH.40")
else:
    print("Input another order")
#Example2
cost=9000
if cost<=1000 and cost>0:
    print("Payment by cash")
elif cost>1000 and cost<=5000:
    print("Payment by M-pesa")
elif cost>5000 and cost<=10000:
    print("payment by credit card")
else:
    print("ERROR:enter cost again")




