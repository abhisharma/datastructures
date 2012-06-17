def UniqueChars(s):
    Set = set()
    for index in range(len(s)):
        if s[index] in Set:
            return "Found duplicate characters in '" + s + "'"
        else:
            Set.add(s[index])
    return "All unique characters in '" + s + "'"

print(UniqueChars("Really"))
print(UniqueChars("Realy"))
print(UniqueChars("Reaccally"))
    