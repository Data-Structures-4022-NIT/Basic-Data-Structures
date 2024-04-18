def merge_sort_second_phase(arr1, arr2):
    new_arr = []
    i = 0
    j = 0
    while(i < len(arr1) or j < len(arr2)):
        if i == len(arr1):
            new_arr.append(arr2[j])
            j += 1
        elif j == len(arr2):
            new_arr.append(arr1[i])
            i += 1
        else:
            if arr1[i] < arr2[j]:
                new_arr.append(arr1[i])
                i += 1
            else:
                new_arr.append(arr2[j])
                j += 1
    return new_arr


print(merge_sort_second_phase([1, 2, 3], [2, 5, 6]))
