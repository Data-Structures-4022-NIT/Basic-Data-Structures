# def MergeSortedArray(Array):
def merge_sorted_arrays(array1, array2):
    counter1=len(array1) - 1
    counter2=len(array2) - 1
    counterMerge =len(array1) + len(array2) - 1

    array1.extend([0] * len(array2))

    while counter1 >= 0 and counter2 >= 0:
        
        if array1[counter1] > array2[counter2]:
            array1[counterMerge] = array1[counter1]
            counter1 -= 1
        else:
            array1[counterMerge] = array2[counter2]
            counter2 -= 1
        counterMerge -= 1

    while counter2 >= 0:
        array1[counterMerge] = array2[counter2]
        counter2 -= 1
        counterMerge -= 1

    return array1

Array1 = [1, 2, 3]
Array2 = [2, 5, 6]
merge_sorted_arrays(Array1, Array2)
print(Array1)