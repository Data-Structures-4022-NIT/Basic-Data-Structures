def RemoveDuplicates(Array):
    lenOfArray=0
    for i in range(0 , len(Array)):
        if(Array[i]!= Array[i-1]):
            lenOfArray +=1
    return lenOfArray         

array = [1 , 1, 2 , 2 , 3, 4 , 5, 5]
print(RemoveDuplicates(array))