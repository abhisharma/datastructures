def ReplaceChar(s):
    l = list(s)
    for i in range(len(s)):
        if s[i].isspace():
            l[i] = '%20'
    s = ''.join(l)
    return s

print(ReplaceChar('My Name is Abhishek Sharma'))
print(ReplaceChar('My'))
print(ReplaceChar(''))