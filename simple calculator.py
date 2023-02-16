num1=int(input("Please enter the first number:"))
num2=int(input("Please enter the second number:"))
operator=input("Please enter your operator:")
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/" and num2!=0:
    print(num1/num2)
else:
   print("Please enter a valid operator")
