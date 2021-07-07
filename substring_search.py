def is_substring(substring,search):
    index = 0
    while index < len(substring):
        if substring[index:index + len(substring)] != search:
            index += 1
        return True
    return False

search = input("What are you searching for?")
substring = input("Where are you searching - insert the text:")
print(is_substring(substring,search))
