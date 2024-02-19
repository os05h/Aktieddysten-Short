from API import Aktiedysten_API
import json
import time

def main():
    """
    This script buys and sells stocks based on predefined conditions.
    It uses the Aktiedysten_API class to interact with the stock market API.
    The script reads stock data from a JSON file and logs transactions to a log file.
    The buying and selling conditions are based on the current and average prices of the stock.
    The script runs in an infinite loop with a 20-second delay between each iteration.
    """
    # Open private json
    private = json.load(open('private.json'))

    # Create API object
    account = Aktiedysten_API(private['Username'], private['Password'], private['Game'])

    # Get stock data
    Stocks = json.load(open('Stock,json'))
    for i in Stocks['Stocks']:
        if i['Name'] == "DOGECOIN":
            Stock1 = i

    # Check if the stock is already bought
    for b in account.GetGameJson()['Assets']:
        if b['Exchange'] == Stock1['MARKET'] and b['Ticker'] == Stock1['ITEM']:
            print("Stock already bought")
            if int(b['ValueGrowth']) > int(Stock1['Change']):
                print(f"Stock is up {b['ValueGrowth']}%")
            else:
                print(f"Stock is down {b['ValueGrowth']}%")
            curentpise = account.GetPrice(Stock1['MARKET'], Stock1['ITEM'], 0)
            Stock1['Bought'] = curentpise * ((100 - int(b['ValueGrowth'])) / 100)
            print(f'You bought the stock for {Stock1["Bought"]}')

    while True:
        # Get Balance
        balance = account.GetCurrencyInBank()
        if balance > 500000:
            # Get average price of stock
            sum = 0
            for i in range(Stock1['Average-Price-Tjeck']):
                sum = sum + account.GetPrice(Stock1['MARKET'], Stock1['ITEM'], i)
            average = sum / Stock1['Average-Price-Tjeck']

            # Get current price of stock
            curentpise = account.GetPrice(Stock1['MARKET'], Stock1['ITEM'], 0)

            # If the stock is not already bought and the current price is less than the average price
            # and the stock is down 0.4% or more
            if Stock1['Bought-Price'] == 0 and curentpise < average and (average - curentpise) / average > Stock1['Change'] / 100:
                # Buy the stock
                account.Buy(Stock1['MARKET'], Stock1['ITEM'], Stock1['MAX-Amount'], "STOCK")
                # Set the bought price
                Stock1['Bought-Price'] = curentpise
                # Log the transaction
                with open('log.txt', 'a') as f:
                    f.write(f'Buy: {Stock1["ITEM"]} for {curentpise}\n')
                # Print the transaction
                print(f'Buy: {Stock1["ITEM"]} for {curentpise}')

            # If the stock is already bought and the current price is more than the bought price
            # and the stock is up 0.4% or more
            if Stock1['Bought-Price'] > 0 and curentpise > Stock1['Bought-Price'] and (curentpise - Stock1['Bought-Price']) / Stock1['Bought-Price'] > Stock1['Change'] / 100:
                # Sell the stock
                account.Sell(Stock1['MARKET'], Stock1['ITEM'], Stock1['MAX-Amount'], "STOCK")
                # Set the bought price to 0
                Stock1['Bought-Price'] = 0
                # Log the transaction
                with open('log.txt', 'a') as f:
                    f.write(f'Sell: {Stock1["ITEM"]} for {curentpise}\n')
                # Print the transaction
                print(f'Sell: {Stock1["ITEM"]} For: {curentpise} profit: {(curentpise - Stock1["Bought-Price"]) * Stock1["MAX-Amount"]}')

            # Wait 20 sec and check again
            time.sleep(20)

if __name__ == "__main__":
    main()
