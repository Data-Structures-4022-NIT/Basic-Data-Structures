class Sparse:
    def __init__(self, matrix):
        self.data = []
        self.row = len(matrix)
        self.column = len(matrix[0])

        for i in range(self.row):
            for j in range(self.column):
                if matrix[i][j] != 0:
                    self.data.append((i, j, matrix[i][j]))

    def Transpose(self):
        transpose= []
        for row,col,value in self.data:
            transpose.append((col,row,value))
        transpose.sort()
        transposed_matrix = [[0 for _ in range(self.row)] for _ in range(self.column)]
        for row, col, value in transpose:
            transposed_matrix[row][col] = value

        return Sparse(transposed_matrix)

    def change_element(self, row, col, new_value):
        for i in range(len(self.data)):
            if self.data[i][0] == row and self.data[i][1] == col:
                if new_value != 0:
                    self.data[i] = (row, col, new_value)
                else:
                    del self.data[i]
                return

        if new_value != 0:
            self.data.append((row, col, new_value))