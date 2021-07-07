def askPassword():
    while input("Password: ") != ("heslo"):
        print("Špatně, hádej znova.")
    print("Bravo!")

askPassword()
