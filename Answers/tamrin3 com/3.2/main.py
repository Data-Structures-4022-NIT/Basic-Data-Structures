n=int(input("Enter len : "))
array=[]
for i in range(n):
    x=int(input(""))
    array.append(x)
k=int(input("Enter Shift : "))
array[:]=array[-k:]+array[:n-k]
for i in range(n):
    print(array[i],end="")
#����� ����? �?� �� �� ����� �� �?���� 