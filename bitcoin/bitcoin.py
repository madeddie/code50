import sys

import requests

try:
    input_amount = float(sys.argv[1])
except:
    sys.exit("Not a valid amount")

try:
    usd_rate = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json().get('bpi').get('USD').get('rate_float')
except requests.RequestException:
    sys.exit("Oops, something went wrong")

amount = input_amount * usd_rate

print(f"${amount:,.4f}")
