# accetps coins in these denominations 25, 10, 5
# ouput how many cents in change
# ignore any input isn't in denominations

# coke price
coke = 50

while coke > 0:

    print(f"Amount Due: {coke}")
    coins = int(input("Insert Coint: "))

    if coins in [25, 10, 5]:
        coke -= coins
    else:
        continue

if coke < 0:
    print(f"Change Owed: {coke * -1}")
else:
    print(f"Change Owed: {coke}")


