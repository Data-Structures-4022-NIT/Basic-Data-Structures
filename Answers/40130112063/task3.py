numbers = [1, 1, 2, 2, 3, 4, 5, 5]
print("input: ", numbers)

n = len(numbers)
temp_list = list(range(n))

i = 0
for j in range(0, n-1):
    if numbers[j] != numbers[j+1]:
        temp_list[i] = numbers[j]
        i += 1

temp_list[i] = numbers[n-1]
i += 1

for j in range(0, i):
    numbers[j] = temp_list[j]

n = i

print("output : ", numbers[:n])
