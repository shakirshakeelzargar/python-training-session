s="helloworld"
#print(s[::-1])

s="helloworld"
#print(s[:])

s="helloworld"
#print(s[3:6])

n="6"

newvar=int(n)
newvar2=float(n)
#print(type(n))
#print(type(newvar))

#print(type(newvar2))
#print(newvar2)



#print(1*5)


#print(6/2)

#print(3**3)

#print(12%5)

#print(15//5)


x=1
y=1

# print(x==y)
# print(x<y)

# print(x<=y)
# print(x>=y)

str1="hello"
str2="Hello"

# print(str1==str2.lower())


x=1
y=6

# print(y>19 or y>28)

y=1
x="6"
# print(type(y)==type(x))


s="shakir"
#print(bool(s))

s=""
#print(bool(s))

n=0
#print(bool(n))

ls=[1,2,3]
#print(bool(ls))

x=None
#print(bool(x))

x=1
y=1
z=1

# if y>x:
#     print(" y is greater than x")
    
# else:
#     print(" x is greater than y")

"""

print("Successfully executed")

if x>y and x>z:
    print(" x is greatest")
elif y>x and y>z:
    print(" y is greatest")
elif z>x and z>y:
    print(" z is greatest")
else:
    print("The numbers are equal")

"""

#print(x)

try:
    #print(5+55+"abc")
    raise Exception("I am raising an error")
except Exception as ex:
    print(f"Some error occured: {ex}")
else:
    print("Addition successful")
finally:
    print("Code executed")


x,y,z=1,2,3
print(x)
print(y)
print(z)

i=1234
str_i=str(i)
rev_str=str_i[::-1]
print(int(rev_str))
































