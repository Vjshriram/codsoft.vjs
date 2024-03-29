print("SIMPLE CALCULATOR")
print('''\n\t MENU\n1.addition \n2.subtraction \n3.multiplication \n4.division''')
x=int(input("enter operation you need to perform :"))
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if(x==1):
    print("the result for addition is:",a+b)
elif(x==2):
    print("the result for subtraction is:",a-b)
elif(x==3):
    print("the result for multiplication is :",a*b)
elif(x==4):
    print("the result for division is :",a/b)
else:
    print("invalid choice")
