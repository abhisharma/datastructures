# This method uses extra buffer
def RemoveDuplicates(s):
    Set = set()
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                Set.add(j)
    
    r = ''            
    for i in range(len(s)):
        if i not in Set:
            r += s[i]
            
    return r

# This method does not use extra buffer but converts string to list
def RemoveDuplicatesOnList(s):
    s = list(s)
    tail = 1
    for i in range(1,len(s)):
        flag = True
        for j in range(0,i):
            if s[i] == s[j]:
                flag = False
                break
            
        if flag:
            s[tail] = s[i]
            tail += 1
    s = ''.join(s)       
    return s[:tail]


print(RemoveDuplicates("Hello"))
print(RemoveDuplicates("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(RemoveDuplicates("aaaabbaaaaccccaaddbcad"))
print(RemoveDuplicates("xyz"))
print(RemoveDuplicates("b"))
print(RemoveDuplicates(""))

print(RemoveDuplicatesOnList("Hello"))
print(RemoveDuplicatesOnList("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(RemoveDuplicatesOnList("aaaabbaaaaccccaaddbcad"))
print(RemoveDuplicatesOnList("xyz"))
print(RemoveDuplicatesOnList("b"))
print(RemoveDuplicatesOnList(""))