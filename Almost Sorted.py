def almostSorted(arr):
    sortarr = deepcopy(arr)
    sortarr.sort()
    
    if sortarr == arr:
        print("yes")
        return
   
    l = r = -1
    
    # left index:
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            l = i
            break
        
    # right index
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:
            r = i
            break 
        
    # check for swap:
    temp = deepcopy(arr)
    
    # swap:
    temp[l], temp[r] = temp[r], temp[l]
    
    if temp == sortarr:
        print("yes")
        print("swap", l+1, r+1)
        return
    
    # check for reverse:
    temp = deepcopy(arr)
    
    # reverse:
    temp = temp[:l] + temp[l:r+1][::-1] + temp[r+1:]
    
    if temp == sortarr:
        print("yes")
        print("reverse", l+1, r+1)
        return
    
    # array can not be sorted
    print("no")
    
           
            
            
            