import datetime

currentDate = datetime.date.today()
domainName = 'FreshFruits.com'
invoiceNumber = 100
qty = 5
unitPrice = 100
totalAmount = qty*unitPrice
discountRate = 10
billAmout = totalAmount - (totalAmount*discountRate/100)
print('=' * 71)
print(domainName)
print(('=' * 35)+('Invoice Bill')+('=' * 25))
print('Invoice No :'+'  '+str(invoiceNumber)+'                         '+'Date :'+' '+str(currentDate))
print('------------------------------------------------------------------------')
print('{0:20} | {1:8} | {2:8} | {3:15}'.format('Item', 'Qty','Unit Price', 'Amount'))
print('{0:20} | {1:8} | {2:8} | {3:15}'.format('Apple', str(qty), str(unitPrice), str(totalAmount)))
print('------------------------------------------------------------------------')
print('Amount :'+' '+str(totalAmount)+'\n'+'Discount Rate:'+' '+str(discountRate)+'%'+'\n'+'Payable Amount :'+' '+str(billAmout))
print('=========================Thanks you for Shopping========================')
