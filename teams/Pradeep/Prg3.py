#To reverse an integer
n=int(input("enter the number :"))
reverse=0
print(f"entered integer : {n}")
try:
    while(n>0):
        x=n%10
        reverse=reverse*10+x
        n=n//10
    
    print(f"reversed integer : {reverse}")
except Exception as e:
    print(f"error occured : {e}")