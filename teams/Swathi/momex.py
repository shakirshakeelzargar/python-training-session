'''1.mom ask me to buy in shop a bread, wheat, tomotoes,stationy items , plastic items
2.shop["groceries","stationary","fancystore"]
3.groceries
buy bread to expire in 4 days buy 4 packets , expires 2 days 2 packets 

4.goto stationary buy paper cardboard(5*8) size in blue colour , 
if blue colur not available then buy white colour,it shold be greater than 5*8
if not finally buy a large paper roll
5.fancy store : shelf boxes of size two feet ,if not avialbe buya any size beteen 2 and 3
6.what are the items  taking to home is output'''

from datetime import datetime

groceryDetails = {
                "p100":{
                    'itemName': 'bread' , 
                    'expireDate': '2020/06/17', 
                    'availableQuantity':3,
                    'isBrown': True,
                    'price':30
                },
                "p101":{
                    'itemName': 'tomotoes' , 
                    'isFresh':True,
                    "PacketQuantity":10,
                    "price":50
                },
                "p102":{
                    'itemName': 'Wheat' , 
                    'availableQuantity': 20,
                    'Brand':["Aata","Ashirvad","patanjali"],
                    "price":60
                }
                }

def get_date_format(eD):
    dateFormat = '%Y/%m/%d'
    tD = datetime.today().strftime(dateFormat)
    t = datetime.strptime(tD, dateFormat)
    expireDate = datetime.strptime(eD, dateFormat)
    d = expireDate - t
    return d.days
    
def get_expire_date(eD,groceryInfo):
    bT=groceryInfo.get("isBrown",None)
    aQ=groceryInfo.get("availableQuantity",None)
    cost=groceryInfo.get("price",None)
    if eD >= 5:
        if bT== True:
            if aQ >= 4:
                print(f"4 packets of Bread cost : {cost*4}")
            else:
                if aQ < 4:
                    print(f"get all the packets of bread {cost*aQ}")
        else :
            if bT == False:
                print("Bread is not Available")
    elif eD >= 2 and eD <= 4:
        if bT== True:
            if aQ >=2:
                print(f"2 packets of Bread cost : {cost*2}")
            else :
                if aQ<2:
                    print(f"get all the packets of bread {cost*aQ}")
        else:
            if bT== True:
                print("Bread is not Available")
    else :
        print("unable to get the bread packets")

def grocery_shop_info(pId,d):
    try :
        groceryInfo=groceryDetails.get(pId.lower(),None)
        itemN=groceryInfo.get("itemName",None)
        eD=groceryInfo.get("expireDate",None)
        if itemN == "bread":
            eD=d(eD)
            get_expire_date(eD,groceryInfo)
        else :
            print("unable to get the bread packets")
    except Exception as e:
        print(f"error message :\n{e}")

def startionary_shop():
    pass
def fancystore_shop():
    pass
if __name__ == "__main__":
    pId="P100"
    grocery_shop_info(pId,get_date_format)

