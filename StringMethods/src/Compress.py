def Compress(s):
    cur = s[0]
    count = 1
    compressed  = ''
    
    for i in range(1, len(s)+1):
        if i < len(s) and cur == s[i]:
            count += 1
        else:
            compressed = compressed + cur + str(count)
            if i < len(s):
                count = 1
                cur = s[i]
            
    if len(compressed) > len(s):
        return s
    else:
        return compressed
    
##############################################################
print(Compress('aabcccccccaaaa'))