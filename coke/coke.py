due = 50
paid = 0

while paid < due:
    print("Amount Due:", due - paid)
    coin = input("Insert Coin: ")
    if coin in ("25", "10", "5"):
        paid += int(coin)
print("Change Owed:", paid - due)
