import sys

try:
    amount = float(sys.argv[1])
except:
    sys.exit("Not a valid amount")

print(amount)
