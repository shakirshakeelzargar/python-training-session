from datetime import date
today = date.today()
name1='Watermelon'
name2='Orange'
q1=5 
q2=7
unit_price1=40
unit_price2=60
print(". "*20,"Welcome to Shop",". "*20)
print(end='\n')
print(" "*35,"*"*5,"Invoice Bill","*"*5)
print(end='\n')
print("     Invoice No: 2345"," "*50,"Date:", today)
print("~ "*20,"Product Details  ","~ "*20,end='\n')
print('           >>  {0:40} >>     {1:5}     >>  {2:5} >>  {3}'.format('Item Name', 'QTY','Unit Price','Amount'))
print(end='\n')
print('           >>  {0:40} >>     {1}kg       >>     ${2:3}    >>    ${3}'.format(name1, q1,unit_price1,unit_price1*q1),end='\n')
print('           >>  {0:40} >>     {1}kg       >>     ${2:3}    >>    ${3}'.format(name2, q2,unit_price2,unit_price2*q2),end='\n')
print("^ "*50)
amount=(unit_price1*q1)+(unit_price2*q2)
print('Total Amount   : $',amount)
if(amount>500):
 Discount=amount*(5/100)
 print("Discount       : $",Discount)
print("Payable Amount : $",amount-Discount)
print(" "*35,"*"*5,"Thank U","*"*5, " "*10,"Contact Us : www.freshfruits.com")