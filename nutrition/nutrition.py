fruits = {
    "apple": 130,
    "avocado": 50,
    "kiwifruit": 90,
    "pear": 100,
    "sweet cherries": 100
}

fruit = input("Which fruitie worries you man? ").strip().lower()
print("Calories:", fruits[fruit])
