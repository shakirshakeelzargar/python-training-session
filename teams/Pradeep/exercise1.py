print("=" * 80)
print("FreshFruits.com")
print('{0:20}  {1:8}  {2:8} '.format('=' * 40, 'Invoice Bill','=' * 40))
print('{0:8}  {1:20}  {2:8} {3:2}  '.format('Invoice No:', 'a7863','Date:','2020-Jun-05'))
print(" ")
print("-" * 80)
print('{0:20} {1:20} {2:20} {3:20}  '.format('Item Name', '|Qty','|Unit Price','|Amount'))
print("-" * 80)
ItemName='Apple'
Qty=25
UnitPrice=40
Amount= Qty * UnitPrice
print('{0:11} {1:12} {2:20} {3:20} '.format(ItemName, Qty, UnitPrice, Amount))
print(" ")
ItemName='Banana'
Qty=15
UnitPrice=10
Amount1= Qty * UnitPrice
print('{0:11} {1:12} {2:20} {3:20} '.format(ItemName, Qty, UnitPrice, Amount1))

print(" ")
print(" ")
print("-" * 80)
TotalAmount=Amount + Amount1
print(f"Total Amount:  {TotalAmount}")
Discount=TotalAmount * 0.05
print(f"Discount:  {Discount}")
PayableAmount=TotalAmount - Discount
print(f"Payable Amount:  {PayableAmount}")
print(" ")
print(" ")
print('{0:20}  {1:8}  {2:8} '.format('=' * 28, 'Thank You for Shopping','=' * 28))
