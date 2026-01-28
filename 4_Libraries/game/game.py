from random import randint

# Get level
while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        else:
            break
    except ValueError:
        pass


number = randint(1, level)

while True:
    try:

        guess = int(input("Guess: "))
        if guess < 1:
            continue
        if guess < number:
            print("Too small!")
            continue
        elif guess > number:
            print("Too large!")
            continue
        else:
            print("just right!")
            break

    except:
        pass

