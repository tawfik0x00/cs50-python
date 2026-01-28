menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0.00

while True:
    try:


        x = input("Item: ").title() # this is the name of item in menu
      
        # we can to search of x in keys of menu
        if x in menu: # KeyError may occur

            total += menu[x]
            print(f"Total: ${total:.2f}")

    except EOFError: # if we get ctrl + d
        print()
        break

    except KeyError: # if the x is not found in the dict we should reprompt
        pass

