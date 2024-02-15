from API import Aktiedysten_API
import json
import time

#Open private json
private = json.load(open('private.json'))

#Login
account = Aktiedysten_API(private['Username'], private['Password'], private['Game'])

#Stocks Simpel buy
Stocks = json.load(open('Stock,json'))
for i in Stocks['Stocks']:
    if(i['nr'] == 1):
        Stock1 = i
#account.Buy(Stock1['MARKET'],Stock1['ITEM'],Stock1['MAX-Amount'],"STOCK")
curentpise = account.GetPrice(Stock1['MARKET'],Stock1['ITEM'], 10)
#print(f"Avage: {sum(curentpise)/len(curentpise)}  Prises: {curentpise}")
bought = 0
while(True):

    if account.GetCurrencyInBank() < 500000:
        break
    else:
        curentpise = account.GetPrice(Stock1['MARKET'],Stock1['ITEM'], 10)
        print(f"Avage: {sum(curentpise)/len(curentpise)}  Prises: {curentpise}")
        if not bought == 0:
            print(f"selsfor profit: {curentpise[len(curentpise)-1]-bought}")
        if sum(curentpise)/len(curentpise)-Stock1["Change"] > curentpise[len(curentpise)-1] and bought == 0:
            bought = curentpise[len(curentpise)-1]
            print("")
            print("Buy")
            print(curentpise[len(curentpise)-1])
            print("")

        if curentpise[len(curentpise)-1]-bought > Stock1["Change"] and not bought == 0:
            
            print("")
            print("Sell")
            print(curentpise[len(curentpise)-1])
            print(f"Profit: {curentpise[len(curentpise)-1]-bought}")
            print("")
            log = open("log.txt", "w")
            log.writelines(f"Profit: {curentpise[len(curentpise)-1]-bought}")
            log.close()
            bought = 0



    time.sleep(20)