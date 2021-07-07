def word_triangle(word):
    lenght = len(word)
    for n in range(lenght):
        print(word[:lenght - n])

word = "abracadabra"

word_triangle(word)
