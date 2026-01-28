# create empty dictionary
my_list = {}
# loop forever
while True:
    try:

        # prompt user for items
        x = input("").strip().upper()

        # if x in my list then add 1 to our old item counter value is int
        if  x in my_list:
            my_list[x] += 1

        # other wise we set a new key and assign one to it first list
        else:
            my_list[x] = 1

    except EOFError:
        # if we recieve a ctr + d EOF then print our dictionary
        for key in sorted(my_list.keys()):
            print(my_list[key], key)
        # break the loop
        break

