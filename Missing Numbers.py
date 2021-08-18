if __name__ == '__main__':
  
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))
    
    # for distict elements
    diff = list((set(arr)-set(brr))) + list((set(brr)-set(arr))) 
    
    # for same elements
    similar =  set(arr).intersection(set(brr))
    
    # check for redundancy
    for i in similar:
        if arr.count(i) != brr.count(i):
            diff.append(i)
    result = ' '.join(map(str,sorted(diff)))
    print(result)
     


   

    
    
