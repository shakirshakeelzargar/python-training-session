# #Divisible by 2

print("Find the Divisible Number")
x= int (input("Enter a number:"))
print (x)
if x%2==0:
    print (f"Number is Divisible by 2")
else:
    print (f"Number is not Divisible by 2")

#Print the lowest integer amoung 4 values

print("Find the Smallest Number")
a= int (input("Enter First Number: "))
b= int (input("Enter Second Number: "))
c= int (input("Enter Third Number: "))
d= int (input("Enter Fourth Number: "))
try:
    if a<b and a<c and a<d:
        print(f"Smallest Number: {a}")
    elif b<a and b<c and b<d:
        print(f"Smallest Number: {b}")
    elif c<a and c<b and c<d:
        print(f"Smallest Number: {c}")
    elif d<a and d<b and d<c:
        print(f"Smallest Number: {d}")
    else:
        if a==b and a==c and a==d:
             raise Exception(f"All values are Equal{a}")
except Exception as e:
    print(f"Error Occured:{e}")

# Reverse an Integer

print("Reverse Integer")
y= int (input("Enter more then 4 Numbers: "))
numToStr = str(y)
print("The Reversed Number:" , int(numToStr[::-1]))