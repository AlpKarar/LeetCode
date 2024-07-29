class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alph = {str(chr(i + 65)): i + 1 for i in range(26)}
        n = len(columnTitle)
        res = 0

        for base in range(n):
            res += (26 ** base) * (alph[columnTitle[n - 1 - base]])
        
        return res