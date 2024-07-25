class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        res = [[0] * n for _ in range(n)]

        for j in range(n):
            for i in range(n - 1, -1, -1):
                res[j][n - 1 - i] = matrix[i][j]
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = res[i][j]