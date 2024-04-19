numbers = [5, 2, 0, 3, 1]

n = len(numbers)

real_sum = n * (n + 1) // 2
numbers_sum = sum(numbers)
missing_number = real_sum - numbers_sum

print("input :", numbers)
print("output: ", missing_number)