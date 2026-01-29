import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line argumetns")
elif len(sys.argv) > 3:
    sys.exit("Too many comman-line argumetns")

output = []

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        # create list of names first and last name
        for row in reader:
            last, first = row["name"].split(",")
            output.append({"first": first.lstrip(), "last": last.lstrip(), "house": row["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as file:

    writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
    writer.writeheader()

    for row in output:
        writer.writerow(row)
