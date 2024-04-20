def Maximum(array):

    MaxSum= sum= array[0]
    start=end,temp= 0

    for i in range(1, len(array)):
        if array[i]> sum+array[i]:
            temp= i
            sum= array[i]
        else:
            sum+= array[i]

        if sum> MaxSum:
            start= temp
            end= i
            MaxSum= sum

    print("Maximum subarray:"+array[start:end+1])
    return MaxSum