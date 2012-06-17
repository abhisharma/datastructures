def PrintParen(left, right, s):
    if left < 0 or right < left:
        return
    
    if left == 0 and right == 0:
        print(s)        
    else:
        if left > 0:
            s = s + '('
            PrintParen(left-1, right, s)
            s = s[:len(s)-1]
            
        if right > left:
            s = s + ')'
            PrintParen(left, right-1, s)
            s = s[:len(s)-1]
            
            
######################################################
PrintParen(3,3,'')