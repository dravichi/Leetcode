class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    for i in range(col):
                        matrix[r][i] = ' ' if matrix[r][i] else 0
                    for i in range(row):
                        matrix[i][c] = ' ' if matrix[i][c] else 0


        for r in range(row):
            for c in range(col):
                if matrix[r][c] == ' ':
                    matrix[r][c] = 0
