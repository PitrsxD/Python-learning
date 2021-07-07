def locate_all(string, target):
    index = 0
    matches = []
    while index < len(string):
        if string[index : index + len(target)] == target:
            matches.append(index)
            index += 1
        else:
            index += 1
    return matches



# Here's a call you can test it with. This should print 4:
print(locate_all('cookbook', 'ook'))
print(locate_all('yesyesyes', 'yes'))
print(locate_all('the upside down', 'barb'))
