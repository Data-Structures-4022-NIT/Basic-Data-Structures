class SparseMatrix:
    def __init__(self, matrix):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.sparse_matrix = self.create_sparse(matrix)

    def create_sparse(self, matrix):
        sparse = []
        for i in range(self.rows):
            for j in range(self.cols):
                if matrix[i][j] != 0:
                    sparse.append((i, j, matrix[i][j]))
        return sparse

    def transpose(self):
        transposed_sparse = []
        for row, col, val in self.sparse_matrix:
            transposed_sparse.append((col, row, val))
        transposed_sparse.sort()
        return transposed_sparse


    def change_element(self, row, col, new_value):
        index = None
        for i, (r, c, val) in enumerate(self.sparse_matrix):
            if r == row and c == col:
                index = i
                break
        if index is not None:
            self.sparse_matrix[index] = (row, col, new_value)
        else:
            self.sparse_matrix.append((row, col, new_value))

    def display(self):
        sparse_matrix = [[0] * self.cols for _ in range(self.rows)]
        for row, col, val in self.sparse_matrix:
            sparse_matrix[row][col] = val
        for row in sparse_matrix:
            print(row)


normal_matrix = [
    [0, 0, 3, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 5]
]

sparse = SparseMatrix(normal_matrix)

print("Original Matrix:")
sparse.display()

print("\nTransposed Matrix:")
transposed = SparseMatrix(sparse.transpose())
transposed.display()

print("\nChanging an element at (0, 2) to 7:")
sparse.change_element(0, 2, 7)
sparse.display()
