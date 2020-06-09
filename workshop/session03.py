# ls=[1,2,3,4,"shakir"]
# print(ls)
# print(ls[::-1])
# print(ls[3])
# ls.append("india")
# print(ls)
# ls.append(20)
# print(ls)
# ls2=["mumbai","chennai"]
# ls.append(ls2)
# print(ls)
# print(ls[-1])
# print(ls[-1][0])



# ls=[1,2,3,4,5,6,7,3,8,9]
# ls.remove(3)
# # ls.pop(7)
# print(ls)

# ls=[1,2,3,4,5]
# ls.pop(0)
# print(ls)

# a=[1,2,3,4,5,6,7]
# print(a[:2])
# print(a[2:])
# b = a[:2] + ["NewItem"] + a[2:]
# print(b)
# print([1]+[4])

# d={"name":"shakir","city":"chennai"}
# print(d)
# print(d["city"])
# print(d["name"])

# d["age"]=23
# print(d["age"])
# print(d)

# print(d.get("country",None))

# ls=[d]
# print(ls)
# print(ls[0]["name"])

# d2={"names":["shakir","Jhon"]}
# # print(d2)
# fruits=["apple","banana","mango","orange"]
# my_fav_fruits=fruits[:]
# my_fav_fruits.append("Litchi")
# print(my_fav_fruits)
# print(fruits)
# ls=[1,2,3,4,5]

# ls=[1,2,3,4,5]
# print(ls)
# ls[0]=100
# print(ls)

# t=(1,2,3,4,5)
# print(t[0])
# print(t+(6,7,8))
# t=([1,2,3],(4,5,6))
# print(type(t[0]))
# print(type(t[1]))

# ls=[1,2,3]
# print(len(ls))


# s={1,2,3,4,5,1,1,1,1,2,2,2}
# print(s)
# print(type(s))
# ls=["apple","apple"]
# new_e=set(ls)
# ls2=list(new_e)
# print(new_e)
# print(ls2)


# fruits=["apple","banana","mango","orange"]

# for f in fruits:
#     print(f)


# n=9
# while n<10:
#     print("its less")
#     # n=n+1



# ls=[1,2,3,4,5]
# ls2=[] 

# for n in ls:
#     if n>2:
#         ls2.append(n)

# print(ls2)

# n1=5
# n2=7
# # var result=n1>n2? "n1 is greater":"n2 is greater"
# print("n1 is greater" if n1>n2 else "n2 is greater")

ls=[1,2,3,4,5,6]
# ls2=[n for n in ls if n>2]
# t=(n for n in ls if n>2)

# for x in t:
#     print(x)

# print(t[::-1])
cities=["","chennai","delhi","mumbai","bangalore","indore","jammu","bengal"]
d={cities[n]:n for n in ls if n>2}
print(d)
countries=["india","nepal","Australia"]
capitals=["delhi","kathmandu","Sydney"]
d={countries[n]:capitals[n] for n in range(len(countries))}
print(d)

for x in range(5,15,2):
    print(x)














