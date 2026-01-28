import inflect
p = inflect.engine()
# Create list of names
names = []
# Loop forever
while True:
    # Get user input
    try:
        name = input("Name: ")
        names.append(name)
    # Create new line and stop the loop
    except EOFError:
        print()
        break

# Printing using inflect module
output = p.join(names)
print("Adieu, adieu, to " + output)