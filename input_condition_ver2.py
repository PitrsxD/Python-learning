import time

def order_breakfeast():
    intro()
    get_order()
    order_again()
    print_pause("Thank you for your visit.")

def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.\n")
    print_pause("Today we have two breakfasts available.\n")
    print_pause("The first is waffles with strawberries and whipped cream.\n")
    print_pause("The second is sweet potato pancakes with butter and syrup.")

def get_order():
    response = valid_input("Please place your order. Would you like waffles or pancakes?\n","pancakes", "waffles")
    if response == "pancakes":
        print_pause("Pancakes it is")
    elif response == "waffles":
        print_pause("Waffle it is")
    print_pause("Your order will be ready shortly.")

def order_again():
        order_againV = valid_input("Would you like to place another order?"
                                  "Please say 'yes' or 'no'.\n",
                                  "yes", "no")
        if "no" in order_againV:
            print_pause("OK, goodbye!")
        elif "yes" in order_againV:
            print_pause("Very good, I'm happy to take another order.")
            get_order()



def valid_input(prompt,option1,option2):
    while True:
        response = input(prompt)
        if option1 == response:
                return response
        elif option2 == response:
            return response
        else:
            print_pause("Sorry, I didnt understand.")


def print_pause(sentence):
    print(sentence)
    time.sleep(1)

order_breakfeast()
