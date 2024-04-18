class Sparse:
    data = []
    origin_Row = 0
    origin_Col = 0

    def __init__(self, matrix):
        self.origin_Row = len(matrix)
        self.origin_Col = len(matrix[0])
        for i in range(self.origin_Row):
            for j in range(self.origin_Col):
                if matrix[i][j] != 0:
                    self.data.append([i, j, matrix[i][j]])

    def transpose(self):
        new_data = [0] * len(self.data)
        if len(self.data) > 0:
            row_size = [0] * self.origin_Row
            for i in self.data:
                row_size[i[1]] += 1
            startOfRow = [0]
            for i in range(1, self.origin_Row):
                startOfRow.append(startOfRow[i - 1] + row_size[i - 1])
            for i in self.data:
                x = startOfRow[i[1]]
                new_data[x] = [i[1], i[0], i[2]]
                startOfRow[i[1]] += 1
        self.data = new_data

    def find_element(self, i, j):
        min_p = 0
        max_p = len(self.data)
        p = (min_p + max_p) // 2
        while min_p != max_p:
            if self.data[p][0] < i or (self.data[p][0] == i and self.data[p][1] < j):
                max_p = p - 1
            elif self.data[p][0] == i and self.data[p][1] == j:
                return p, 0
            else:
                min_p = p + 1
            p = (min_p + max_p) // 2
        if self.data[p][0] == i and self.data[p][1] == j:
            return p, 0
        else:
            return -1, p

    def change_element(self, i, j, new_data):
        index, near = self.find_element(i, j)
        if new_data == 0:
            if index != -1:
                new_data.pop(index)
        else:
            if index != -1:
                self.data[index][2] = new_data
            else:
                flag = False
                for p in range(max(near-1, 0), min(near+2, len(self.data))):
                    if self.data[p][0] > i or (self.data[p][0] == i and self.data[p][1] > j):
                        flag = True
                        break
                if flag:
                    self.data.insert(p, [i, j, new_data])
                else:
                    self.data.insert(p+1, [i, j, new_data])


arr2d = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
first_sparse = Sparse(arr2d)
print(first_sparse.data)
first_sparse.transpose()
print(first_sparse.data)

first_sparse.change_element(1, 0, 2)
print(first_sparse.data)
