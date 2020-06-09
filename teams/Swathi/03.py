#1. Write custom program to imitate a do while loop
  
def imitate_do_while_loop(i):
    try :
        if i!=0:
            while True:  
                print(i)  
                i = i + 1  
                if(i > 5):  
                    break   
    except Exception as e:
        print(f"error occured : {e}")
imitate_do_while_loop(1)
imitate_do_while_loop(6)


#2. Print greatest integer out of 4 numbers using ternary operator

n1 = 100
n2 = 250
n3 = 300
n4 = 500
def greatest_integer(n1,n2,n3,n4):
    mx = (n1 if (n1 > n2 and n1 > n2 and n1 > n4)  
         else (n2 if (n2 > n3 and n3 > n4)  
         else (n3 if n3 > n4 else n4))) 
    
    print(f"Greatest number {n1},{n2},{n3},{n4} is : {mx}")
greatest_integer(n1,n2,n3,n4)

#3. print all prime numbers between 1-100
l =1  
u = 100  
  
def get_prime_numbers(lower,upper):
    for num in range(lower,upper + 1):  
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:  
                print(num) 
get_prime_numbers(l,u)

#4. Print the smallest and largest number from a list
#1

list1 = [10, 20, 4, 45, 99] 
list1.sort() 
print(f"Smallest element is:{list1[0]}") 
print(f"highest element is:{list1[-1]}") 

#2

ls=[10,4,6,36,190]
print(f"smallest value : {min(ls)}")
print(f"largest value : {max(ls)}")

#5. Create a dictionary containing the following keys: fruits, countries. 
# The values to these keys should be in a list. Create 
# a similar dictionary out of this where the values are sorted in ascending order

d1={
    "fruits":["mango","apple","banana"],
    "countries":["India","Australia","Bangladesh"]
}

def dict_sort(d):
    f=d.get("fruits",None)
    c=d.get("countries", None)
    f=f.sort()
    c=c.sort()
    print(d)
dict_sort(d1)