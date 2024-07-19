class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins = []

        for i in range(len(matrix)):
            cur_min = float("inf")
            x = 0
            y = 0

            for j in range(len(matrix[0])):
                if matrix[i][j] < cur_min:
                    cur_min = matrix[i][j]
                    x = i
                    y = j
            
            mins.append([x, y])
        
        res = []

        for indexes in mins:
            cur_max = matrix[indexes[0]][indexes[1]]

            for i in range(len(matrix)):
                if cur_max < matrix[i][indexes[1]]:
                    cur_max = matrix[i][indexes[1]]
            
            if cur_max == matrix[indexes[0]][indexes[1]]:
                res.append(cur_max)

        return res