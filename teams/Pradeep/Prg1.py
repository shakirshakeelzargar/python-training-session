# number is exactly divisible by 2
n=int(input("Please enter the number: "))
try:
    if n%2==0:
        print(f"Given number is divisible by 2")
    else :
        print(f"Given number is not divisible by 2")
except Exception as e:
    print(f"error occured : {e}")