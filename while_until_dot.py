"""
def until_dot(string):
    index = 0
    while index < len(string) and string[index] != ".":
        index += 1
    return string[:index]
"""

def until_dot(string):
    ch = 0
    for ch in range(len(string)):
        if string == ".":
            return string[:ch]
    return string

print(until_dot("This is a sentence. This is another."))
print(until_dot("No dots here"))
