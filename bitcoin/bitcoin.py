import sys

import requests

try:
    amount = float(sys.argv[1])
except:
    sys.exit("Not a valid amount")

try:
    ...
except requests.RequestException:
    ...
