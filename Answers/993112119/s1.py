def find_miss(input_arr):
    bool_arr = [False] * (len(input_arr) + 1)
    for i in input_arr:
        bool_arr[i] = True
    for i in range(len(bool_arr)):
        if not bool_arr[i]:
            return i
    return -1

print(find_miss([5, 2, 0, 3, 1]))
