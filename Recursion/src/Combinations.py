def Combinations(s):
    if len(s) == 1:
        return s
    first = s[0]
    perms = Combinations(s[1:])
    
    l = list()
    for item in perms:               
        newitem = item + first
        l.append(newitem)
 
    l.append(first)
    l.extend(perms)           
    return l
        
##########################################
perms = Combinations('abcd')
for item in perms:
    print(item)     
    
print("Count is "+ str(len(perms)))