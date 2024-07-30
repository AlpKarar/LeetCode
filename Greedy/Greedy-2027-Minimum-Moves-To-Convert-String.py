class Solution:
    def minimumMoves(self, s: str) -> int:
        res = 0        
        i = 0

        while i < len(s):
            res += 1 if s[i] == "X" else 0
            i += 3 if s[i] == "X" else 1
        
        return res