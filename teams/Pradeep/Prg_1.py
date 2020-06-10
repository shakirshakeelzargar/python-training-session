# 1.Write a python function which takes a list as an argument and returns the sum of elements in the list
# creating a list 

#list values
list1 = [15,6,89,76,65] 
  
# using sum() function 
def summ(list1):
    a=0
    for i in list1:
        a=a+i
    return a
sumVal=summ(list1)
print(f"sum of list values : {sumVal}")
