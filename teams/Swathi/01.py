
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
    print("========================================================================")
    print(storename)
    print("==========================Invoice Bill==================================")
    print("Invoice No :"+" "+str(i_no)+"                                "+"Date :"+" "+str(d))
    print("------------------------------------------------------------------------")
    print("Item Name"+"     "+"Qty"+"     "+"Unit Price"+"     "+"Amount")
    print("------------------------------------------------------------------------")
    print(I_Name+"          "+str(qty)+"          "+str(up)+"         "+str(amt))
    print("------------------------------------------------------------------------")
    print("Amount :"+" "+str(amt)+"\n"+"Discount :"+" "+dis+"\n"+"Payable Amount :"+" "+str(pamt))
    print("=========================Thanks you for Shopping========================")
invoice_bill(invoice_no, today)


