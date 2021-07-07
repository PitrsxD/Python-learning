# Write your function definition here
word = 0

def start_K(word):
    if word[0] == "K":
        print("True")
    else:
        print("False")

# A function call like this should return True:
# print(start_K("Kelly"))
word = "Kelly"
print(word)
start_K(word)

# And one like this should return False:
# print(start_K("Abe"))

word = "Abe"
print(word)
start_K(word)
