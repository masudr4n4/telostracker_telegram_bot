import requests
import json
import time
import requests
import datetime
from time import sleep
import sys
set_price = 0.91
last_sent_message_time = datetime.datetime(2021, 12, 22, 22, 49, 38, 499491)

BOT_TOKEN = '2059690124:AAGxuB9LEC-abMzDKqHI9IzdABgkioogunY'
# CHAT_ID = '-573286459'
CHAT_ID = '511293895'
url = "https://api.coingecko.com/api/v3/"
coins = url +"coins/markets?vs_currency=usd&ids=telos"
def telegram_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' +BOT_TOKEN + '/sendMessage?chat_id=' + str(CHAT_ID) + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def get_price():
    return requests.get(coins).json()[0]['current_price']

url = "https://telos.caleos.io/v1/chain/get_table_rows"
payload = {"json":True,"code":"amm.swaps","scope":"amm.swaps","table":"pairs","lower_bound":"23","upper_bound":"","index_position":1,"key_type":"","limit":1,"reverse":False,"show_payer":False}

previous_price = 0

while True:
    try:
        res = requests.get(url,data=json.dumps(payload))
        apx_price = res.json()['rows'][0]['price0_last']
        price = round(float(apx_price),3)
        if previous_price != price:
            current_apx_price = price/round(float(get_price()),3)
            price_in_usd = round(current_apx_price,3)
            message =f"@masudrana0 Telos valueChangedTo: {price},USD: {price_in_usd}$"
            print(price_in_usd)
            telegram_sendtext(message)
            previous_price = price
    except Exception as e:
        try:
            telegram_sendtext(f"Something went wrong! {e}")
        except:
            pass


