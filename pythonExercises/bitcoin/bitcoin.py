import requests
import json
import sys

if len(sys.argv)!=2:
    sys.exit("Value is not an integer")
try:
    n=float(sys.argv[1])
except ValueError:
    exit("Value is not an integer")

try:
    dictionary=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    vol1=dictionary["bpi"]
    vol2=vol1["USD"]
    coin_value=float(vol2["rate"].replace(",",""))
    convertion=n*coin_value
    print(f"${convertion:,.4f}")




except requests.RequestException:
    print("aaa")