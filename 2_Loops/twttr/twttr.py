text = input("Input: ")

newtext = ""
for c in text:
    
    if c in ['A', 'a', 'I', 'i', 'O', 'o', 'U', 'u', 'E', 'e']:
        continue
    else:
        newtext += c

print(f"Output: {newtext}")