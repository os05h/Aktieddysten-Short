# Aktieddysten-Short

## Description
This bot for Aktiedysten makes shorting shares super easy.

## How to set up
Set up an account on [aktiedysten.dk](https://aktiedysten.dk/) and join a game
Create a `private.json` file and fill out the information.

```json
{
    "Username" : "",
    "Password" : "",
    "Game" : ""
}
```

In the `Stock.json` file is where you spesifey the stock

Eksampel
```json
{
    "Stocks": [
        {
            "Name": "DOGECOIN",
            "MARKET": "CRYPTO",
            "ITEM": "DOGE",
            "MAX-Amount": 10,
            "Change": 0.004,
            "Average-Price-Tjeck": 10,
            "Bought-Price": 0
        }
    ]
}
```
The name has to be the same in run.py ln 23

```py
# Get stock data
Stocks = json.load(open('Stock,json'))
for i in Stocks['Stocks']:
    if i['Name'] == "DOGECOIN":
        Stock1 = i
```