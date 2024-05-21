class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        
        substring = s[:3]
        cur = set([letter for letter in substring])
        res = 1 if len(cur) == 3 else 0

        for i in range(3, len(s)):
            substring = s[i-2:i+1]
            cur = set([letter for letter in substring])

            if len(cur) == 3:
                res += 1
        
        return res