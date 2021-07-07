def strComp(long,short):
    for position in range(len(short)):
        if long[position] != short[position]:
            return False
    return True

print(strComp("apple","app"))
print(strComp("manatee","mango"))
