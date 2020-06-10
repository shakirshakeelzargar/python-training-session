'''1.mom ask me to buy in shop a bread, wheat, tomotoes,stationy items , plastic items
2.shop["groceries","stationary","fancystore"]
3.groceries
buy bread to expire in 4 days buy 4 packets , expires 2 days 2 packets 

4.goto stationary buy paper cardboard(5*8) size in blue colour , 
if blue colur not available then buy white colour,it shold be greater than 5*8
if not finally buy a large paper roll
5.fancy store : shelf boxes of size two feet ,if not avialbe buya any size beteen 2 and 3
6.what are the items  taking to home is output'''

#input
from datetime import datetime
today = datetime.date.today()
format_str = "%y-%m-%d"
print(format_str)
d={"grocery_shop":[{"itemname":"bread","expire_date":"2020-06-07","availablity_qty":20,"isbrown":True,"cost":20}]}
items=d.get("grocery_shop",None)
for i in items:
    if i.get("itemname")=="bread":
        print(i.get("itemname"))
        #d=datetime.datetime.strptime(i.get("expire_date"), format_str)
        #d=d.date()
        #print(d)
        #if d == 2 :

#print(today)





