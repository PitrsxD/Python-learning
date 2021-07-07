def count_substring(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index:index + len(target)] == target:
            total += 1
            index += len(target)
        else:
            index += 1
    return total

# Here's a call you can test it with. This should print 4:
print(count_substring('AAAA', 'AA'))
