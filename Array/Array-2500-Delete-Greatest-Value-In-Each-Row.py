class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0
        
        for i in range(len(grid)):
            grid[i] = sorted(grid[i])
        
        for j in range(len(grid[0]) - 1, -1, -1):
            colMax = 0

            for i in range(len(grid)):
                if grid[i][j] > colMax:
                    colMax = grid[i][j]
            
            res += colMax
                
        return res