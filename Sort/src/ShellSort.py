import random
def ShellSort(input):
    n = len(input)
    m = n//3
    while m >= 1:
        for i in range(2*m-1,n,m):
            x = input[i]
            j = m
            while i >= j and x < input[i-j]:
                input[i-j+m] = input[i-j]
                j = j + m
            input[i-j+m] = x         
        m = m // 2
        
#####################################
input = [1,2,4,6,2,11,100,5,7]
print(input)
ShellSort(input)
print(input)

n=1000
input = list()
for _ in range(n):
    input.append(random.randint(1, n))
    
print(input)
ShellSort(input)
print(input)
