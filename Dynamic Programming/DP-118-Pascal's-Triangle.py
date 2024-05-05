class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(1, numRows + 1):
            cur = [1] * i

            if len(res) > 1:
                for j in range(1, i - 1):
                    cur[j] = res[-1][j] + res[-1][j - 1]

            res.append(cur)    
        
        return res