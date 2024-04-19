num1 = [1, 2, 3]
num2 = [2, 5, 6]

print("inputs : ", "\nnum1 = ", num1, "\nnum2 = ", num2)

n = len(num1)
m = len(num2)

i = n - 1
j = m - 1
k = m + n - 1

num1.extend([0] * m)

while i >= 0 and j >= 0:
    if num1[i] >= num2[j]:
        num1[k] = num1[i]
        i -= 1
    else:
        num1[k] = num2[j]
        j -= 1
    k -= 1

while i >= 0:
    num1[k] = num1[i]
    k -= 1
    i -= 1


while j >= 0:
    num1[k] = num2[j]
    k -= 1
    j -= 1


print("num1 = ", num1)
