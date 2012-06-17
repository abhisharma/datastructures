def NthFib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*NthFib(n-1)

def NthFibWithTailRecursion(n,result):
    if n == 1 or n == 0:
        print(result)
    else:
        return NthFibWithTailRecursion(n-1, result*n)
    
################################################
print(NthFib(0))
NthFibWithTailRecursion(7,1)