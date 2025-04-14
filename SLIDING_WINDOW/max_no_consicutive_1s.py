def max_no_cons_1s(arr):
    size = len(arr)
    
    l = 0
    r = 0
    max_cons_1s = 0
    while(r < size):
        if(arr[r] != 1):
            max_cons_1s = max(max_cons_1s, r - l)
            l = r+1
            
        if(r == size-1 and arr[r] == 1):
            max_cons_1s = max(max_cons_1s, r-l+1)
        r += 1
        
    return max_cons_1s

print(max_no_cons_1s([1, 1, 1, 0, 0, 1, 1, 1, 1]))