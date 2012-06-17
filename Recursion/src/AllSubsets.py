def ComputeSubsets(s):
    if len(s) == 0:
        return list()
    
    first = s.pop()
    allsubs = ComputeSubsets(s)
    
    moresubsets = list()
    for item in allsubs:
        newlist = list(item)    # Copy each list
        newlist.append(first)   # append the first element
        moresubsets.append(newlist)        
    
    allsubs.append(list(first))   
    allsubs.extend(moresubsets)
    
    return allsubs


###############################################################
allsubs = list()
s = set(['a', 'b', 'c', 'd', 'e'])
allsubs = ComputeSubsets(s)

for item in allsubs:
    print(sorted(item))     
    
print("Subset size is "+ str(len(allsubs)))       