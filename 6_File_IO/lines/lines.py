import sys

# check command line argument
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

sys.argv[1] = sys.argv[1].rstrip()

# check end
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

num_lines = 0

try:
    with open(sys.argv[1], "r") as file:
        for line in file:
           if line.isspace() or line.lstrip().startswith("#"):
               continue
           else:
               num_lines += 1

except FileNotFoundError:
    sys.exit("File does not exist")

print(num_lines)
