# Get the user input
answer = input("File name: ").strip().lower()

# Check for each extension and print the right file type
if answer.endswith(".gif"):
    print("image/gif")
    
elif answer.endswith(("jpg", "jpeg")):
    print("image/jpeg")
    
elif answer.endswith(".png"):
    print("image/png")
    
elif answer.endswith(".pdf"):
    print("application/pdf")
    
elif answer.endswith(".txt"):
    print("text/plain")
    
elif answer.endswith(".zip"):
    print("application/zip")
    
else:
    print("application/octet-stream")
