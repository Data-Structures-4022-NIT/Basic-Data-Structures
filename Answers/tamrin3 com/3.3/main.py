def bsearch(array, x, i, low, high):
    test = False
    if low <= high:
        mid = (low + high) // 2
        if array[mid] > x:
            return bsearch(array, x, i, low, mid - 1)
        elif array[mid] < x:
            return bsearch(array, x, i, mid + 1, high)
        elif array[mid] == x and i != mid:
            test = True
    if test:
        return 1
    else:
        return 0

def main():
    array = [1, 1, 2, 2, 3, 4, 5, 5]
    n = len(array)
    low = 0
    high = n - 1
    counter = 0
    x = 0
    for i in range(n):
        x = bsearch(array, array[i], i, low, high)
        if x == 1:
            counter += 1
            array[i]=0
    i = 0
    #�� �?��� �� ����� ʘ���? �� ��� ���?� �� �� ���?� ��� �?��?� � ��� �� �� ��� �� ��� �ǁ �?��?�
    while i < len(array):
     if array[i] == 0:
        array.pop(i)
     else:
        i += 1
    print(len(array))
if __name__ == "__main__":
    main()
    #      ���?� nlogn   �� �?��� �� ����� �� ��    
# ?� ����� �� ����� �� ��� �� �� �� ���� ?� ��?��? �э �� ���?� �� �� ��� ����� �� ����� nlogn ���