class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def helper(row_index):            
            for j in range(len(isConnected[0])):
                if isConnected[row_index][j] == 1:
                    isConnected[row_index][j] = 0
                    helper(j)

        res = 0

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    helper(j)
                    res += 1
        
        return res