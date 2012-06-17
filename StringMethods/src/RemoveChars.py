def RemoveChars(inputStr, strToRemove):
    mydict = dict()
    for i in range(len(strToRemove)):
        mydict[strToRemove[i]] = 1
    newstr = ''
    for i in range(len(inputStr)):
        if mydict.get(inputStr[i]) == None:
            newstr += inputStr[i]
           
    return newstr
        
#######################################
print(RemoveChars('Battle of the Vowels: Hawai vs. Grozny', 'aeiou'))