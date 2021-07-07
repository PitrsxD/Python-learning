# import libraries
import time
import random
import game_inv

# global variables
chEnemy = ""
chWeapon = "dagger"
yourHP = 10
enemyHP = 10
attackNumber = 2
alreadyInCave = 0


# start the game
def start_game():
    call_enemy(game_inv.enemies)
    intro()
    path()


# intro to the story
def intro():
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that {chEnemy} is somewhere around here, and"
                "has been terrifying the nearby village.")


# where to go - path
def path():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave. ")
    print_pause("What would you like to do?")
    pathNumber = input("(Please enter 1 or 2)\n")
    choose_path(pathNumber)


# choose the path
def choose_path(pathNumber):
    global alreadyInCave
    # if player already is in cave or now
    if alreadyInCave == 1 and pathNumber == "2":
        print_pause("You are already in Cave. Choose other path.\n")
        path()
    # player choose where to go
    else:
        if pathNumber == "1":
            to_the_house()
        elif pathNumber == "2":
            to_the_cave()
        else:
            pathNumber = input("(Please enter 1 or 2)")
            choose_path(pathNumber)


# choose the house
def to_the_house():
    print_pause(f"You knock on the door and {chEnemy} opened it.")
    print_pause("You have two option fight(1) or run(2).")
    option = input("Which one will you choose?\n")
    if option == "1":
        fight()
    elif option == "2":
        run()
    else:
        print_pause("Sorry I didn't understand.")
        to_the_house()


# choose the cave
def to_the_cave():
    global attackNumber
    global alreadyInCave
    # get new weapon
    call_weapon(game_inv.weapons)
    print_pause("You entered to the cave.")
    print_pause(f"Under big pile of dirt, you found {chWeapon}.")
    print_pause(f"Your attack is now {attackNumber}.")
    print_pause("Where would you go next?")
    alreadyInCave = 1
    path()


# restart
def restart():
    again = input("Do you want play the game again? Yes or No?\n")
    again.lower()
    if again == "yes":
        print_pause("Restarting the game...!")
        # reseting all global variables
        global chEnemy
        chEnemy = ""
        global chWeapon
        chWeapon = "dagger"
        global yourHP
        yourHP = 10
        global enemyHP
        enemyHP = 10
        global attackNumber
        attackNumber = 2
        global alreadyInCave
        alreadyInCave = 0
        start_game()
    elif again == "no":
        return
    else:
        print_pause("Sorry I didn't understand.")
        restart()


# fight with your enemy
def fight():
    global yourHP
    global enemyHP
    print_pause(f"You decided to fight with {chEnemy}.")
    print_pause("Now lets throw a dice to see if you manage to attack.")
    print_pause("You need 3 and less to attack.")
    while yourHP > 0 and enemyHP > 0:
        print_pause("Your HP is:" + str(yourHP))
        print_pause("Enemy HP is:" + str(enemyHP))
        # throwing dice if it is attacking enemy or you
        if throwDice() <= 3:
            your_attack()
        else:
            enemy_attack()
    else:
        if yourHP <= 0:
            print_pause("You lost!")
            restart()
        elif enemyHP <= 0:
            print_pause("You won!")
            restart()


# you are attacking enemy
def your_attack():
    print_pause("\nYou are attacking!")
    global attackNumber
    global enemyHP
    enemyHP = enemyHP - attackNumber
    print_pause(f"Enemy lost {attackNumber} HP")
    return


# enemy is attacking on you
def enemy_attack():
    print_pause("\nBeware! Enemy is attacking on you!")
    global attackNumber
    global yourHP
    yourHP = yourHP - 3
    print_pause("You lost 3 HP.")
    return


# run from battle
def run():
    print_pause(f"You decided to run from {chEnemy}.")
    print_pause("Now lets throw a dice to see if you manage to escape.")
    print_pause("You need 3 and less to run away succesfully.")
    # succes of running from battle
    if throwDice() <= 3:
        print_pause("Hurray! You managed to escape.")
        restart()
    else:
        print_pause("You shamefuly died during your try...")
        restart()


# player throw a dice
def throwDice():
    diceNumber = random.randint(1, 6)
    print_pause("Number on dice:" + str(diceNumber))
    return diceNumber


# randomly selected enemy
def call_enemy(enemy):
    global chEnemy
    chEnemy = (random.choice(enemy))


# randomly slected weapon
def call_weapon(weapon):
    global chWeapon
    chWeapon = (random.choice(weapon))
    global attackNumber
    attackNumber = 1 + random.randint(1, 4)
    return


# pause between sentences
def print_pause(sentence):
    print(sentence)
    time.sleep(1.7)


start_game()
