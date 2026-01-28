fruit = input("Item: ").strip().lower()

calories = {
    "apple": 130,
    "avocado": 50,
    "banana": 10,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

if fruit in calories: # search in keys.
    # print the value if found
    print(f"Calories: {calories[fruit]}")