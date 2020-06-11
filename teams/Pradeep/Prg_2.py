# 2.	Create a function which performs the basic arithmatic operations(+,-,/,*). 
# It takes three inputs, num1, num2 and operator symbol as string For ex: func(2,3,"+")

#Defining Functions
n1=int(input("enter the number1: \n"))
n2=int(input("enter the number2: \n"))
def arith_func(n1,n2,op):
    if op == "+":
        print(f"The value of Addition is: {n1+n2}")
    elif op == "-":
        print(f"The value of Subtraction is: {n1-n2}")
    elif op == "*":
        print(f"The value Multiply is: {n1*n2}")
    else:
        print(f"The value Division is: {n1/n2}")

arith_func(n1,n2,"+")
arith_func(n1,n2,"-")
arith_func(n1,n2,"*")
arith_func(n1,n2,"/")