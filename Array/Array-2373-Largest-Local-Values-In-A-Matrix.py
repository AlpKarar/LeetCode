class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                curMax = 0

                for k in range(3):
                    for m in range(3):
                        if grid[i + k][j + m] > curMax:
                            curMax = grid[i + k][j + m]
                
                res[i][j] = curMax
        
        return res