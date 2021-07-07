##def good_length_ver1(word):
    if len(word) > 8:
        if len (word) < 64:
            return "nice password, yo"
        return "This is really much too long for a password. I mean, it's really secure, but I don't want to type this much every time I log in, okay?"
    return "2short"


word = input("New Password: \n")
##print(good_length(word))

# This should print False, because it's under eight characters.
print(good_length("2short"))
def good_length_ver(word)


# This should print True, since it's between eight and 64 characters long:
print(good_length("nice password, yo"))

# This should print False, since it's over 64 characters long:
print(good_length("This is really much too long for a password. I mean, it's really secure, but I don't want to type this much every time I log in, okay?"))
