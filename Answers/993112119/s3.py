def remove_duplicates(input_arr):
    i = 0
    while(i < len(input_arr)-1):
        if input_arr[i] == input_arr[i+1]:
            input_arr.pop(i)
        else:
            i += 1
    return len(input_arr)


arr = [1, 1, 2, 2, 3, 4, 5, 5]
print(remove_duplicates(arr))
print(arr)
