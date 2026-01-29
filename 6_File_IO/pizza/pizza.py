import sys
import csv
from tabulate import tabulate

if len(sys.argv) > 2:
    print("Too many command-line arguments")
elif len(sys.argv) < 2:
    print("Too few command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

# place to save our values
table = []

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file) # return a list of lists

        for row in reader:
            table.append(row)

except FileNotFoundError:
    sys.exit("File doesn't exist")

# we will print the table

print(tabulate(table[1:], headers=table[0], tablefmt="grid" ))