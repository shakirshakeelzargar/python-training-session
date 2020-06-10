# ls=["bangladesh","australia","india"]
# print(ls)
# ls.sort()
# print(ls)
# ls.sort(reverse=True)
# print(ls)

# ls.insert(1, "china")
# print(ls)


# num=[3,6,5,1,2,3,4]
# print(min(num))
# print(max(num))

# d={"name":"shakir"}

# x,y=1,2
# for k,v in d.items():
#     print(k,v)

# for k in d.keys():
#     print(k)

# for v in d.values():
#     print(v)


# n=1
# while True:
#     print(n)
#     n=n+1
#     if n==5:
#         break

# print("Executed")
    

# #print all odd numbers from 1-20

# for n in range(1,21):
#     if n%2==0:
#         continue
#     print(n)

# for n in range(1,5):
#     pass

# print("Executed")

def sayhello(name,country):
    print(f"Hello {name}. I am in {country}")
    return "Function Output"

output=sayhello("shakir","India")
print(output)


def add(a,b):
    summ=a+b
    return summ

# output=add(3,2)
# print(output)


# def test(name="Python"):
#     print(name)

# test("Python 3.8")


# def test(*arg):
#     for n in arg:
#         print(n)

# test(1,2,3,4,5,6)


# def person(**address):
#     print(address)

# person(state="chennai",city="Nandanam")

# print(a+b)
# a=1
# b=2

# def maths(addition):
#     o=addition(1,2)
#     print(o)

# maths(add)


# def person(name="shakir",age=23):
#     print(name,age)

# person(age=23,name="shakir")

# x=lambda a,b : a+b
# print(x(2,3))

# # class person:
#     #Attributes and methods
#     #Attributes are variables within a class
#     # methods are functions within a class

#     def address(self):
#         print("India")


# per1=person()
# per2=person()

# person.address(per1)
# person.address(per2)

# per1.address()


class person:
    def __init__(self,name):
        print("I am inside init")
        self.name=name

    def printname(self):
        print(self.name)


p1=person("shakir")
p1.printname()





