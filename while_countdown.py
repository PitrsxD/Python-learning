import time

def countdown(number):
    while number > 0:
        time.sleep(1)
        print(number)
        number -= 1
    print("Blastoff!")

number = input("Write number: ")
countdown(int(number))
