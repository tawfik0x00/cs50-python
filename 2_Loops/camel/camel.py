# Get camelCase name
camelCase = input("camelCase: ")

# create new string to save our new name
snake_case = ""

# iterate over our camelCase to get the uppercase Value
for c in camelCase:
    if c.isupper(): # return true if is upper
        snake_case += "_" + c.lower() # if true convert to lower
        # and add _ before thie letter
    else:
        # otherwise concatenate this letter to our snake_case string
        snake_case += c.lower()

print(snake_case)
