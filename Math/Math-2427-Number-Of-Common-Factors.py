class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0

        for c in range(min(a, b), 0, -1):
            if a % c == 0 and b % c == 0:
                res += 1
        
        return res