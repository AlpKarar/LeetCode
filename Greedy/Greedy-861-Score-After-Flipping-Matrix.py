class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
        
        for j in range(m):
            count_zero = 0
            count_one = 0

            for i in range(n):
                if grid[i][j] == 1:
                    count_one += 1
                else:
                    count_zero += 1
            
            if count_zero > count_one:
                for i in range(n):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                    else:
                        grid[i][j] = 1
        

        res = 0

        for row in grid:
            row = [str(i) for i in row]
            res += int("".join(row), 2)
        
        return res