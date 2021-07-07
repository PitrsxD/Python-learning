import time

def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.\n")
    print_pause("Today we have two breakfasts available.\n")
    print_pause("The first is waffles with strawberries and whipped cream.\n")
    print_pause("The second is sweet potato pancakes with butter and syrup.")

def askForFood():
    foodInput = input("Please place your order. Would you like waffles or pancakes?\n")
    condition(foodInput.lower())
    print_pause("Your order will be ready shortly.")
    return foodInputNext

def condition(food):
    index = 0
    while index < len(food):
        if food[index:index + len("pencake")] == "pancake":
            print_pause("Pancakes it is")
            return
        elif food[index:index + len("waffle")] == "waffle":
            print_pause("Waffles it is!")
            return
        else:
            index += 1
    foodAgain = input("Sorry, I didnt understand.\nDo you want pankcakes or waffles?")
    condition(foodAgain)

def print_pause(sentence):
    print(sentence)
    time.sleep(1)

foodInputNext = ""
askForFood()
while True:
    foodInputNext = input("Do you want something else? Yes or No?").lower()
    if foodInputNext == "yes":
        askForFood()
    elif foodInputNext == "no":
        break
    else:
        print_pause("Sorry I didnt understand. Can you repeat it again?")
print_pause("Thank you for your visit.")
