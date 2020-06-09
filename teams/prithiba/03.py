#Print greatest integer out of 4 numbers using ternary operator

a,b,c,d = 12,34,88,88
max = (a if (a >= b and a >= c and a >= d)  
         else (b if (b >= a and b >= c and b >= d)  
         else (c if (c >= a and c >= b and c >= d) else d))) 
print("Largest Number:", max)

#Print all prime numbers between 1-100

a,b,i  = 1,100,0
for x in range(a, b, 1):
   if x > 1:
       for index in range(2, x):
           if ((x % index) == 0):
               break
       else:
           i=i+1
           print(x)
           continue
           
print("Total Prime number between 1 to 100  - {}  ".format(i))

#Print the smallest and largest number from a list

list = [1,4,6,0]
#print(max(list))
#print(min(list))

list.sort()
print("smallest_Number:{0} and largest_Number : {1}".format (list[0],list[-1]))

#Input: d1={ "fruits":["mango","apple","banana"], "countries":["India","Australia","Bangladesh"] }
#Output: d2={ "fruits":["apple","banana","mango"], "countries":["Australia","Bangladesh","India"] }

d1={
    "fruits":["mango","apple","banana"],
    "countries":["India","Australia","Bangladesh"]
}
d2=d1["fruits"]
d3=d1["countries"]
d2.sort()
d3.sort()
d4={"fruits":d2, "countries" : d3}
print(d4)
