class MergeSort:
    def merge_sort(self, arr):
        if arr is None or len(arr) <= 1:
            return
        temp = [0] * len(arr)
        self.sort(arr, temp, 0, len(arr) - 1)

    def sort(self, arr, temp, low, high):
        if low < high:
            mid = low + (high - low) // 2
            self.sort(arr, temp, low, mid)
            self.sort(arr, temp, mid + 1, high)
            self.merge(arr, temp, low, mid, high)

    def merge(self, arr, temp, low, mid, high):
        for i in range(low, high + 1):
            temp[i] = arr[i]

        i = low
        j = mid + 1
        k = low

        while i <= mid and j <= high:
            if temp[i] <= temp[j]:
                arr[k] = temp[i]
                i += 1
            else:
                arr[k] = temp[j]
                j += 1
            k += 1

        while i <= mid:
            arr[k] = temp[i]
            i += 1
            k += 1

if __name__ == "__main__":
    arr = [7,4,2,5,3,0,6]
    sorter = MergeSort()
    sorter.merge_sort(arr)
    n=len(arr)
    for i in range(n):
        if arr[i] == i:
            print("")
        elif arr[i]!=i:
            print("not found:")
            print(i)
            break
            
