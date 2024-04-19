class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        defaultZeroPositions = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    defaultZeroPositions.add((i,j))
        
        for position in defaultZeroPositions:
            row, col = position

            for c in range(len(matrix[0])):
                matrix[row][c] = 0
            
            for r in range(len(matrix)):
                matrix[r][col] = 0