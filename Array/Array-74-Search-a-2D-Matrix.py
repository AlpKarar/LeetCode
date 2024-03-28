class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r1 = 0
        r2 = len(matrix) - 1
        mr = 0
        isBreak = False

        while r1 <= r2:
            mr = r1 + (r2 - r1) // 2

            if matrix[mr][0] <= target and target <= matrix[mr][-1]:
                isBreak = True
                break
            elif target < matrix[mr][0]:
                r2 = mr - 1
            else:
                r1 = mr + 1
        
        if not isBreak:
            return False
        
        l = 0
        r = len(matrix[0])

        while l <= r:
            m = l + (r - l) // 2

            if matrix[mr][m] == target:
                return True
            elif matrix[mr][m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False