class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        for i in range(row):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(row):
            matrix[i].reverse()
        