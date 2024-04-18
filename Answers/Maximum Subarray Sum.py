def MaximumSubarraySum(Array):
    n=len(Array)
    Max=Array[0]
    for i in range(0,n):
        s=Array[i]
        if ( s >= Max ):
            Max=s
        j=i+1
        while(j < n):
            s = s + Array[j]
            if ( s >= Max ):
                Max=s
            j=j+1

    return Max

# array = [-2, -1, -3, 4, -1, 2, 1, -5, 4]
array=[1 ,5 ,-1 , -50 , 3 , 4 ,7 , -5]
print(MaximumSubarraySum(array))
