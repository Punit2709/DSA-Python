def max_sum_k_size_window(arr:list, size:int) -> int:
    sum = 0
    for i in range(size):
        sum += arr[i]
    
    l = 0
    r = size    
    maxSum = sum
    
    while(r < len(arr)):
        sum -= arr[l]
        sum += arr[r]
        l += 1
        r += 1
        
        maxSum = max(maxSum, sum)
        
    return maxSum

def max_sum_k_size_window_2(arr:list, k:int) -> int:
    l,r = 0, 0
    maxSum = 0
    sum = 0
    while(r < len(arr)):
        sum += arr[r]
        
        if(r - l + 1 < k):
            r += 1
        elif r - l + 1 == k:
            maxSum = max(maxSum, sum)
            sum -= arr[l]
            l += 1
            r += 1
        
    return maxSum
    

arr = [2, 5, 1, 8, 2, 9, 1]
print(max_sum_k_size_window(arr, 3))
# print(max_sum_k_size_window_2(arr, 3))
