#  To find if a number is exactly divisible by 2 
x=49
try:
    if(x%2!=0):
        raise exception("Note:")
except:
    print("Odd Number")
else:
    print("Even Number")

# Using 4 integers and print the lowest integer value, if all are equal, raise an exception 
a,b,c,d =22,22,22,22
try:
    if(a==b or b==c or c==d or a==c or a==d or d==b or a==d):
        raise exception("Problem:")
    elif(a<b and a<c and a<d):
        print("a - lowest Number")
    elif(b<a and b<c and b<d):
        print("b - lowest Number")
    elif(c<a and c<b and c<d):
        print("c - lowest Number")
    elif(d<a and d<b and d<c):
        print("d - lowest Number")
except:
        print("More than one lowest number")

#Reverse an integer
n1,n2=134,0
try:
    while(n1>0):
        p=n1%10
        n2=n2*10+p
        n1=n1//10
    if(n2==0):
          raise exception("Negative Value")
except:
    print("Invalid")
else:
    print(n2)