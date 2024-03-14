import inflect

p = inflect.engine()
name_list = []
while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        print()
        break
final_list = p.join(name_list)
print("Adieu, adieu, to " + final_list)
