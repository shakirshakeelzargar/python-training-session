#1. Write a python function which takes a 
# list as an argument and returns the sum of elements in the list

ls=[1,2,3,4,5,6]

def sum_func(ls):
    c=0
    for i in ls:
        c+=i
    return c
sum_value=sum_func(ls)
print(f"sum of list values : {sum_value}")

#2. Create a function which performs the 
# basic arithmatic operations(+,-,/,*). It takes three inputs, num1, num2 and 
# operator symbol as string
# For ex:
# func(2,3,"+")
num1=int(input("enter the number 1 value : \n"))
num2=int(input("enter the number 2 value : \n"))

def arithmetic_fun(num1, num2, op):
    try :
        if op == "+":
            print(f"sum of two values is : {num1+num2}")
        elif op == "-":
            print(f"difference of two values is : {num1-num2}")
        elif op == "*":
            print(f"product of two values is : {num1*num2}")
        elif op == "/":
            print(f"division of two values is : {num1/num2}")
        elif op == "**":
            print(f"exponential value is : {num1**num2}")
        else :
            print(f"module division of two values is : {num1%num2}")
    except Exception as e:
        print(f"error occured : {e}")
arithmetic_fun(num1,num2,"+")
arithmetic_fun(num1,num2,"-")
arithmetic_fun(num1,num2,"*")
arithmetic_fun(num1,num2,"/")
arithmetic_fun(num1,num2,"%")
arithmetic_fun(num1,num2,"**")

#3. You are given lengtgh and breadth of a rectangular feild. Create a class 
# which is constructed using length and breadth. The class should contain a 
# method names get_area.Calling this method should return the area of the 
# rectangular feild.
class Rectangular:
    def __init__(self,l,b):
        print("init method")
        self.l=l
        self.b=b

    def get_area(self):
        return self.l*self.b
    def get_perimeter(self):
        return 2*(self.l+self.b)
r=Rectangular(4,5)
a=r.get_area()
p=r.get_perimeter()
print(f"area of rectangle : {a}")
print(f"perimeter of rectangle : {p}")
