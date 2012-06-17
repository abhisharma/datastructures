def Permutations(s):
    if len(s) == 1:
        return s
    first = s[0]
    perms = Permutations(s[1:])
    
    l = list()
    for item in perms:
        for i in range(len(item)+1):
            if i > 0:
                prefix = item[:i]
            else:
                prefix = ''
            if i < len(item):
                suffix = item[i:]
            else:
                suffix = ''
                
            newitem = prefix + first + suffix
            l.append(newitem)
            
    return l
        
##########################################
perms = Permutations('abc')
for item in perms:
    print(item)     
    
print("Count is "+ str(len(perms)))