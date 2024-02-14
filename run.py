from API import Aktiedysten_API
import json

#Open private json
private = json.load(open('private.json'))

#Login
account = Aktiedysten_API(private['Username'], private['Password'], private['Game'])

#Stocks
Stocks = json.load(open('Stock,json'))
for i in Stocks['Stocks']:
    if(i['nr'] == 1):
        Stock1 = i
account.Buy(Stock1['MARKET'],Stock1['ITEM'],Stock1['MAX-Amount'],"STOCK")