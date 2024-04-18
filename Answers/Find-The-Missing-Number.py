def find_missing_number(Array):
    n = len(Array)
    sum = n * (n + 1) // 2
    sumOfElementArray = 0
    for element in Array:
        sumOfElementArray = sumOfElementArray + element
    missingNumber = sum - sumOfElementArray
    return missingNumber

array = [0 , 1 , 2 , 3 , 5]
print(find_missing_number(array))