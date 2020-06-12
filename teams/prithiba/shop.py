from datetime import date, timedelta
current_date = date.today()
brown_specific_date = date(2020,6,16 )
normal_specific_date = date(2020,6,13 )
days_brown= (brown_specific_date - current_date).days
days_normal=(normal_specific_date - current_date).days
Grocery_list= []
finished = False
print("Welcome to Grocery_list")
while not finished:
    item= input('Enter an item : ')
    if len(item) == 0:
        finished = True
    else:
        if(item=="bread" ):
             type_bread = (input("type of bread :").lower)
             qty_brownBread = 10
             qty_normalBread = 10
             
             if(type_bread=="brown" and days_brown>5 and qty_brownBread>0):
                qty_brownBread = qty_brownBread-4
                Grocery_list.append(item)
                else:
                    print("Not Available")
             if(type_bread=="normal" and days_normal>3 and qty_normalBread>0):
                qty_normalBreadread = qty_normalBread-2
                Grocery_list.append(item)
               
                else:
                    print("Not Available")
Grocery_list.append(item)
print("Thanks for Shop")
print()
Stationary_list= []
finished = False
print("Welcome to Stationary_Shop")
while not finished:
    item= input('Enter an item : ')
    if len(item) == 0:
        finished = True
    else:
        if(item=="Paper_cardboard"):
            size=input("Enter Size: ")
            color = input("Enter color:")
            if( size == "5*8" and color =="Blue"):
                print("Available -- Item : {0},Size: {1}, Color:{2}".format(item,size,color))
            if( size > "5*8" and color == "White"):
                print("Available --Item : {0},Size: {1}, Color:{2}".format(item,size,color))
    Stationary_list.append(item)
print("Thank for shop")
print()
FancyStore_list = []
finished =False
print("Welcome to FancyStore_Shop")
while not finished:
    item=input("Enter an item :")
    if len(item) ==0:
        finished = True
    else:
        if(item=="self_box"):
            size =input("Enter the size: ")
            if(size == "4"):
                print("Available--Item : {0},size: {1}".format(item,size))
            elif(size<"4"):
                print("Available--Item : {0},size: {1}".format(item,size))
    FancyStore_list.append(item)
print()
print('Your Stationary_List:')
print('*' * 20)
for item in Stationary_list:
    print(item)
print()
print('Your FancyStore_List:')
print('*' * 20)
for item in FancyStore_list:
    print(item)
print()
print('Your GroceryList:')
print('-' * 18)
for item in Grocery_list:
    print(item)
