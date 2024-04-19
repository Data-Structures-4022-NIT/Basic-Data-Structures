numbers = [1, 2, 3, 4, 5]
k = 2
print(f"input : {numbers}, k = {k}")

n = len(numbers)
k = k % n
numbers[:] = numbers[-k:] + numbers[:-k]


print("output :", numbers)