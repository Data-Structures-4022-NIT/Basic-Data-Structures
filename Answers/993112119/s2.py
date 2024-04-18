def rotate_array_1(input_arr, k):
    for i in range(k):
        val = input_arr.pop()
        input_arr.insert(0, val)


def rotate_arr_2(input_arr, k):
    new_arr = input_arr[-k:] + input_arr[0:-k]
    return new_arr


def rotate_arr_3(input_arr, k):
    new_arr = []
    for i in range(len(input_arr) - k, len(input_arr)):
        new_arr.append(input_arr[i])
    for i in range(len(input_arr) - k):
        new_arr.append(input_arr[i])
    return new_arr


arr = [1, 2, 3, 4, 5]
rotate_array_1(arr, 2)
print(arr)

print(rotate_arr_2([1, 2, 3, 4, 5], 2))

print(rotate_arr_3([1, 2, 3, 4, 5], 2))
