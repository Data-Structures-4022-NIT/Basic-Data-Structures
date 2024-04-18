def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    rotated_arr = [0] * n
    for i in range(k):
        rotated_arr[i] = arr[n-k+i]

    for i in range(k, n):
        rotated_arr[i] = arr[i-k]
    
    return rotated_arr

array = [1, 2, 3, 4, 5]
k = 2
print(rotate_array(array, k))

      

      
    