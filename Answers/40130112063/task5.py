numbers = [-2, -1, -3, 4, -1, 2, 1, -5, 4]
print(numbers)

max_so_far = numbers[0]
curr_max = numbers[0]
start = 0
end = 0

for i in range(1, len(numbers)):
    curr_max = max(numbers[i], curr_max + numbers[i])
    max_so_far = max(max_so_far, curr_max)

print("output :", max_so_far)
