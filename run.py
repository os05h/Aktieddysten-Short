from API import Aktiedysten_API
import json
import time

#Open private json
private = json.load(open('private.json'))

#Create API object
account = Aktiedysten_API(private['Username'], private['Password'], private['Game'])


#Get stock data
Stocks = json.load(open('Stock,json'))
for i in Stocks['Stocks']:
    if i['Name'] == "DOGECOIN":
        Stock1 = i


#function to buy stock
#account.Buy(Stock1['MARKET'],Stock1['ITEM'],Stock1['MAX-Amount'],"STOCK")

#function to sell stock
#account.Sell(Stock1['MARKET'],Stock1['ITEM'],Stock1['MAX-Amount'],"STOCK")

#function to get the price of a stock
#account.GetPrice(Stock1['MARKET'],Stock1['ITEM'], 1)

#function to get account balance
#account.GetCurrencyInBank()

#function to get portfolio
#account.GetGameJson()



#account.Buy(Stock1['MARKET'],Stock1['ITEM'],Stock1['MAX-Amount'],"STOCK")
#curentpise = account.GetPrice(Stock1['MARKET'],Stock1['ITEM'], 0)

#Simpele stock buy and sell
#loging the transactions to log.txt
#buying 1 stock
#selling 1 stock
#only if there is a profit of 0,4% or more
#and if the stock is not already bought
#there should alvays be 500000 in the account
#make sure to log the transactions to log.txt
#make sure to make is it can be calibratedet white a json file
#make sure to make it so it can be run in a loop

#check if the stock is already bought 
for b in account.GetGameJson()['Assets']:
    if b['Exchange'] == Stock1['MARKET'] and b['Ticker'] == Stock1['ITEM']:
        print("Stock already bought")
        if int(b['ValueGrowth']) > int(Stock1['Change']):
            print(f"Stock is up {b['ValueGrowth']}%")
        else:
            print(f"Stock is down {b['ValueGrowth']}%")

while False:
    #get Balance
    balance = account.GetCurrencyInBank()
    if balance > 500000:
        #get average price of stock
        for i in range(Stock1['Average-Price-Tjeck']):
            sum = sum + account.GetPrice(Stock1['MARKET'],Stock1['ITEM'], i)
        average = sum / Stock1['Average-Price-Tjeck']

        #get current price of stock
        curentpise = account.GetPrice(Stock1['MARKET'],Stock1['ITEM'], 0)

        #if the stock is not already bought and the current price is less than the average price
        