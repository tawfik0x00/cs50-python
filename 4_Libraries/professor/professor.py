import random


def main():
    level = get_level()
    score = simulate_game(level)

    print("Score: ", score)


def get_level():

    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n

        except:
            pass

def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)

    elif level == 2:
        return random.randint(10, 99)

    else:
       return random.randint(100, 999)

def simulate_round(x, y):

    count_tries = 1

    while count_tries <= 3:
        try:
            answer = int(input(f" {x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x+y} ")
    return False

def simulate_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x = generate_integer(level)
        y = generate_integer(level)
        response = simulate_round(x, y)

        if response == True:
            score += 1

        count_round += 1
    return score

if __name__ == "__main__":
    main()

