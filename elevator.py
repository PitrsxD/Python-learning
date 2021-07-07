#import libraries
import time

#variables
items = []

#whole story
def story():
    intro()
    select_floor()

#intro - new job
def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")
    print_pause("Please enter the number for the floor you would like to visit:")

#Select the floor
def select_floor():
    print_pause("1. Lobby")
    print_pause("2. Human resources")
    print_pause("3. Engineering department")
    floor = input("")
    intFloor = int(floor)
    input_floor(intFloor)

#select the floor loop
def input_floor(floor):
    if floor == 1:
        first_floor()
    elif floor == 2:
        second_floor()
    elif floor == 3:
        third_floor()
    else:
        print_pause("Sorry try it again.\n")

#first floor
def first_floor():
    print_pause("You push the button for the first floor.\n")
    print_pause("After a few moments, you find yourself in the lobby.\n")
    if "ID card" in items:
        print_pause("The clerk greets you, but she has already given you your"\
                    "ID card, so there is nothing more to do here now.")
    else:
        print_pause("The clerk greets you and gives you your ID card.")
        items.append("ID card")
    print_pause("Where would you like to go next?")
    select_floor()

#second floor
def second_floor():
    print_pause("You push the button for the second floor.\n")
    print_pause("After a few moments, you find yourself in the human resources department.\n")
    if "Handbook" in items:
        print_pause("The HR folks are busy at their desks."\
                    "There doesn't seem to be much to do here.")
    else:
        print_pause("The head of HR greets you")
        if "ID card" in items:
            print_pause("He looks at your ID card and then gives you a copy of the employee handbook.")
            items.append("Handbook")
        else:
            print_pause("He has something for you, but says he can't"\
                        "give it to you until you go get your ID card.")
    print_pause("Where would you like to go next?")
    select_floor()

#third floor
def third_floor():
    print_pause("You push the button for the third floor.\n")
    print_pause("After a few moments, you find yourself in the engineering department.\n")
    if "ID card" in items:
        print_pause("You use your ID card to open the door.\n"\
                    "Your program manager greets you and tells you that you need to have a copy of the"\
                    "employee handbook in order to start work.")
        if "Handbook" in items:
            print_pause("Fortunately, you got that from HR!\n"\
                        "Congratulatons! You are ready to start your new job as vice president of engineering!")
        else:
            print_pause("They scowl when they see that you don't have it, and send you back to the elevator.")
            return
    else:
        print_pause("Unfortunately, the door is locked "
                        "and you can't get in.")
        print_pause("It looks like you need some kind of "
                        "key card to open the door.")
        print_pause("You head back to the elevator.")
    print_pause("Where would you like to go next?")
    select_floor()


#print_pause
def print_pause(sentence):
    print(sentence)
    time.sleep(0.7)

story()
