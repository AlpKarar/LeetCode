class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * n for _ in range(m)]

        for i in range(m):
            matrix[i][0] = 1
        
        for j in range(n):
            matrix[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
        
        return matrix[m - 1][n - 1]