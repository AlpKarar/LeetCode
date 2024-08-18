class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0

        for i in range(n):
            res += mat[i][i]

        for i in range(n):
            res += mat[n - i - 1][i]
        
        return res if n % 2 == 0 else res - mat[n // 2][n // 2]