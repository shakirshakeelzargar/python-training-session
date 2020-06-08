from datetime import date
print (("<")*22, "Invoice Bill", (">")*23)
print ("")
print ("Sample Receipt")
print ("1407, Some St")
print ("Some City")
print ("Some State")
print ("www.samplereceipt.com")
print (("=")*60)
print ("Cashier :" , "#13")
print ("Customer :" , "VIP")
print (("=")*60)
print ("{0:15}  {1:15}  {2:15}  {3:15}".format("ProductName","Units","UnitPrice","Amount"))
print (("-")*60)
productName =  (["PS4 Console" , "Controller"])
Units1 = 1
Units2 = 2
unitPrice1 = 27000
unitPrice2 = 3500
Amount1 = Units1*unitPrice1
Amount2 = Units2*unitPrice2
TotalAmount= Amount1 + Amount2
Discount= TotalAmount * 0.05
TotalPayable= TotalAmount - Discount
print ("{0:10}  {1:9}  {2:15}  {3:15}".format(productName[0], Units1 , unitPrice1 , Amount1))
print ("{0:10}  {1:10}  {2:15}  {3:15}".format(productName[1], Units2 , unitPrice2 , Amount2))
print (("-")*60)
print (f"Total Amount: {TotalAmount}")
print (f"Discount Price: {Discount}")
print (f"Total Payable: {TotalPayable}")
print (("=")*60)
print (("")*15, "NO RETURNS WITHOUT RECEIPT", ("")*15)
print ("")
print (("<")*15, "Thanks for Shopping with Us", (">")*16)