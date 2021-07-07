def replace_substring(string,toReplace,replaceS):
    list = []
    index = 0
    while index < len(string):
        if string[index: index + len(toReplace)] == toReplace:
            index += len(toReplace)
            list.append(replaceS)
        else:
            list.append(string[index])
            index += 1
    return "".join(list)

print(replace_substring('Hot SPAM!drop soup, and curry with SPAM!plant.', 'SPAM!', 'egg'))
print(replace_substring("The word 'definately' is definately often misspelled.", 'definately', 'definitely'))
