def remove_string(string,toRemove):
    list = []
    index = 0
    while index < len(string):
        if string[index: index + len(toRemove)] == toRemove:
            index += len(toRemove)
        else:
            list.append(string[index])
            index += 1
    return "".join(list)

print(remove_string("SPAM!HelloSPAM! worldSPAM!!","SPAM!"))
