def getChar(key, index):
    if key == 0:
        return '0'
    elif key == 1:
        return '1'
    elif key == 2:
        if index == 0:
            return 'A'
        if index == 1:
            return 'B'
        if index == 2:
            return 'C'
    elif key == 3:
        if index == 0:
            return 'D'
        if index == 1:
            return 'E'
        if index == 2:
            return 'F'
    elif key == 4:
        if index == 0:
            return 'G'
        if index == 1:
            return 'H'
        if index == 2:
            return 'I'
    elif key == 5:
        if index == 0:
            return 'J'
        if index == 1:
            return 'K'
        if index == 2:
            return 'L'
    elif key == 6:
        if index == 0:
            return 'M'
        if index == 1:
            return 'N'
        if index == 2:
            return 'O'
    elif key == 7:
        if index == 0:
            return 'P'
        if index == 1:
            return 'R'
        if index == 2:
            return 'S'
    elif key == 8:
        if index == 0:
            return 'T'
        if index == 1:
            return 'U'
        if index == 2:
            return 'V'
    elif key == 9:
        if index == 0:
            return 'W'
        if index == 1:
            return 'X'
        if index == 2:
            return 'Y'
N = 0
digits = dict()
       
def ComputeDigits(number):
    global digits
    global N
    while number > 0:
        k = number%10
        number = number//10
        digits[N] = k
        N = N+1
    
def PrintPhone(result,index):  
    global digits
    global N
      
    if index == N:
        print(result)
    else:
        digit = digits[index]
        for i in range(3):
            ch = getChar(digit,i)
            result = ch + result
            PrintPhone(result,index+1)
            result = result[1:]
            if digit == 1 or digit == 0:
                break
            
def PrintPhone_NoRecur():  
    global digits
    global N

    result = ''
    for i in range(N):
        digit = digits[i]
        result = getChar(digit,0) + result
    count = 0 
      
    while True:
        print(result)
        count += 1
        
        if count == pow(3,N):
            break

        for i in range(0,N):
            digit = digits[N-i-1]
            
            prefix = ''
            if i > 0:
                prefix = result[:i]
            
            suffix = ''
            if i < N-1:
                suffix = result[i+1:]
             
            if result[i] == getChar(digit,2) or result[i] == 0 or result[i] == 1:
                result = prefix + getChar(digit,0) + suffix
                continue
            if result[i] == getChar(digit,0): 
                result = prefix + getChar(digit,1) + suffix
                break
            if result[i] == getChar(digit,1): 
                result = prefix + getChar(digit,2) + suffix
                break
            
        
    print(count)
             
             
####################################
ComputeDigits(523)
#PrintPhone('', 0)
PrintPhone_NoRecur()
    