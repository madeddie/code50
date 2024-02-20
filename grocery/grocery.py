grocery_list = {}

while True:
    try:
        item = input().strip().upper()
        grocery_list.setdefault(item, 0)
        grocery_list[item] += 1
    except EOFError:
        print(grocery_list)
