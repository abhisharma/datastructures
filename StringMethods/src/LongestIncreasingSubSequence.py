def LongestIncreasingSubSequence(l):
    q = dict()  # list of length of the subsequence ending at pos(which is key of dict entry)
    prev = dict()
    for i in range(len(l)):
        q[i] = 0
        prev[i] = 0
    
    ########## Real Work #############
    for i in range(len(l)):
        for j in range(i):
            x = q[j]+1
            if l[j] < l[i] and q[i] < x:
                q[i] = x
                prev[i] = j;
    ########## Real Work #############
    
    max = 0      
    pos = 0
    for i in range(len(l)):
        if q[i] > max:
            max = q[i]
            pos = i
 
    print('Max length:: '+ str(max))
    
    ans = list()
    while max >= 0:
        ans.append(l[pos])
        pos = prev[pos]
        max -= 1
        
    return [item for item in reversed(ans)]
    
    
    
    
##########################
print(LongestIncreasingSubSequence([ 1, 2, 3, 2, 4, 3, 5, 4, 2, 7, 6]))