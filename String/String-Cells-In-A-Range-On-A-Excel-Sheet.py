class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alphs = {chr(i+65):i for i in range(26)}
        alph_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        col_start = alphs[s[0]]
        col_end = alphs[s[-2]]
        row_start = int(s[1])
        row_end = int(s[-1])

        res = []

        for col_idx in range(col_start, col_end + 1):
            for row_idx in range(row_start, row_end + 1):
                res.append(alph_upper[col_idx] + str(row_idx))
        
        return res