
# importing necessary packages
import random
import string
import datetime

# getting the current date execution
today = datetime.date.today()

#getting random generated Invoice number
N=1
ch = ''.join(random.choices(string.ascii_lowercase, k = N)) 
num=random.randint(1,1000)
invoice_no=ch+str(num)

#writing a funtion to print online shopping details
def invoice_bill(i_no, d):
    storename = "FreshFruits.com"
    I_Name = "Apple"
    qty=34
    up=50
    amt=1500
    dis="10%"
    pamt=amt-(amt*10//100)
    s=" "*25
    s2=" "*10
    print("="*62)
    print(storename)
    print("="*25+"Invoice Bill"+"="*25)
    print(f"Invoice No :{i_no}{s}Date : {d}")
    print("-"*62)
    print(f"Item Name{s2}Qty{s2}Unit Price{s2}Amount")
    print("-"*62)
    print(f"{I_Name}  {s2}  {qty}  {s2}  {up}  {s2}  {amt}")
    print("------------------------------------------------------------------------")
    print(f"Amount : {amt}\nDiscount : {dis}\nPayable Amount : {pamt}")
    print("="*25+"Thanks you for Shopping"+"="*25)
invoice_bill(invoice_no, today)


