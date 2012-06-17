def MakeChange(n, denom):
    next = 0
    if denom == 25:
        next = 10
    elif denom == 10:
        next = 5
    elif denom == 5:
        next = 1
    elif denom == 1:
        return 1
    
    ways = 0
    i = 0
    while i*denom <= n:
        ways = ways + MakeChange(n-denom*i, next)
        i += 1
            
    return ways

################################
print(MakeChange(100,25))