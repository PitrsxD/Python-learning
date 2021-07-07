def locate_first(target, string):
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            return index
        else:
            index += 1
    return -1


# Here's a call you can test it with. This should print 4:
print(locate_first('ook', 'cookbook'))
print(locate_first('base', 'all your bass are belong to us'))
