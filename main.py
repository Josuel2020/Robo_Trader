from binance.client import Client
from keys import api_key, api_secret

client = Client(api_key, api_secret)


status = client.get_account_status()
print(status)

# to get account's informations, use:
info = client.get_account()
#for item in info:
#    print(item)

# to see avaible's balance in account, use:
#print(info["balances"])



for ativo in info["balances"]:
    if float(ativo["free"]) > 0:
        print(ativo)
