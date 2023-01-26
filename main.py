from binance.client import Client
from binance.enums import *
from keys import api_key, api_secret

client = Client(api_key, api_secret)




# getting informations of account
info = client.get_account()

# getting the balances of account
list_balance = info["balances"]
for ativo in list_balance:
    if float(ativo["free"]) > 0:
        print(ativo)

#creating an order
#print(list_balance["asset"])


order = client.create_order(
    symbol='BTCBRL',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    transactTime=1000,
    quantity = 0.1,
    price = 100,
    )

print(order)
