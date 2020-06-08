
#1. Write a program to  find if a number is exactly divisible by 2

#getting user input
num=int(input("enter the number :\n"))
try:
    if num!=0:
        if num%2==0:
            print(f"number is divisible by 2 : {num}")
        else :
            print(f"number is not divisible by 2 : {num}")
except Exception as e:
    print(f"error occured : {e}")

#2. Take 4 integers and print the lowest integer value, if all are equal,
#  raise an exception stating all values are equal.

num1=20
num2=2
num3=6
num4=8
try:
    if num1<num2 and num1<num3 and num1<num4:
        print(f"lowest value : {num1}")
    elif num2<num1 and num2<num3 and num2<num4:
        print(f"lowest value : {num2}")
    elif num3<num1 and num3<num2 and num3<num4:
        print(f"lowest value : {num3}")
    elif num4<num1 and num4<num2 and num4<num3:
        print(f"lowest value : {num4}")
    else :
        if num1==num2 and num1==num3 and num1==num4:
            raise Exception(f"all values are equal {num1}")

except Exception as e:
    print(f"error occured : {e}")

#3. Write a program to reverse an integer
n=int(input("enter the number : \n"))
rev=0
print(f"entered integer : {n}")
try:
    while(n>0):
        a=n%10
        rev=rev*10+a
        n=n//10
    
    print(f"reversed integer : {rev}")
except Exception as e:
    print(f"error occured : {e}")





