def main():
    # get text
    text = input()

    # print result
    print(convert(text))

def convert(x):
    # assign new value of x after replace to x
    x = x.replace(":)", "🙂").replace(":(", "🙁")
    
    # return x to user
    return x

main()
