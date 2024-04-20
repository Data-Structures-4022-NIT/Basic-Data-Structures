def Rotate(array, k):
    n=len(array)
    k=k%n

    RotateArray = [0] * n

    for i in range(n):
        if i < k:
            RotateArray[i]= RotateArray[n- k+i]
        else:
            RotateArray[i]= array[i-k]

    for i in range(n):
        array[i] = RotateArray[i]