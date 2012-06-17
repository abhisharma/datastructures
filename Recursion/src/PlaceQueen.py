N = 4
Cols = dict()
count  = 0

def PrintBoard():
    global count
    
    for j in range(N):
        for k in range(N):
            if k == Cols[j]:
                print("Q", end= '\t')
            else:
                print("0", end= '\t')
        print("\n") 
    print("Done\n")
    count += 1   
        
def CheckPlace(i):
    for k in range(i):
        colDiff = abs(Cols[k]-Cols[i])
        rowDiff = abs(i-k)
        if colDiff == 0 or colDiff == rowDiff: 
            return False
    return True

def PlaceQueen(i):
    if i == N:
        PrintBoard()
    else:
        for j in range(N):
            Cols[i] = j
            if CheckPlace(i):
                PlaceQueen(i+1)
                
                
###########################################
PlaceQueen(0)
print("Total Count is " + str(count))