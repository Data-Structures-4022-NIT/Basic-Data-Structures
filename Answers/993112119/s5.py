def max_sub_array(arr):
    # if array is filled by negative numbers
    maxy = arr[0]
    is_negative = True
    max_index = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            is_negative = False
            break
        if arr[i] > maxy:
            maxy = arr[i]
            max_index = i
    if is_negative:
        return maxy, [maxy]

    # and what if not?
    first = end = first_max = end_max = 0
    sum_till = max_sum = 0
    for i in range(1, len(arr)):
        if sum_till + arr[i] > arr[i]:
            end = i
            sum_till += arr[i]
        else:
            sum_till = arr[i]
            first = end = i
        if max_sum < sum_till:
            first_max = first
            end_max = end
            max_sum = sum_till
    return max_sum, arr[first_max:end_max + 1]


print(max_sub_array([-2, -1, -3, 4, -1, 2, 1, -5, 4]))
