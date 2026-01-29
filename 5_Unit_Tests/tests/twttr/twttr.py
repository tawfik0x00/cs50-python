def main():
    text = input("Input: ")
    short = shorten(text)
    print("Output:", shorten(text))

def shorten(word):

    short = ""

    for c in word:
        if c in ['A', 'a', 'I', 'i', 'O', 'o', 'U', 'u', 'E', 'e']:
            continue
        else:
            short += c

    return short

if __name__ == "__main__":
    main()