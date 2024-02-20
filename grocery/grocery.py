grocery_list = {}

while True:
    try:
        item = input().strip().upper()
        grocery_list.setdefault(item, 0)
        grocery_list[item] += 1
    except EOFError:
        for item in sorted(grocery_list.items()):
            print(item[1], item[0])
        exit()
