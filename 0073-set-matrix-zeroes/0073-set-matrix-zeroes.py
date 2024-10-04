class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        aSet = set()
        m, n = len(matrix), len(matrix[0])

        def handle(i, j):
            print("000i, j:", i, j)
            for k in range(n):
                handleAdjacent(i, k)
            for k in range(m):
                handleAdjacent(k, j)

        def handleAdjacent(i, j):
            if matrix[i][j] == 0:
                return
            if i >= 0 and i < m and j >= 0 and j < n:
                matrix[i][j] = 0
            aSet.add(i*n + j)

        for i in range(m):
            for j in range(n):
                if i*n+j in aSet:
                    continue
                if matrix[i][j] == 0:
                    handle(i, j)
        
