def green_room():
    print("You are in the green room.")


def blue_room():
    print("You are in the blue room.")


def choose_room():
    choice = input("Would you like to go to the green room or the blue room?\n")
    return choice

def call_room():
    choice = choose_room()
    if choice == 'green':
        print("You are in the green room.")
    elif choice == 'blue':
        print("You are in the blue room.")
    else:
        print("I don't know what that is.")
        call_room()

call_room()
