class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = {}

        for char in s:
            c[char] = c.get(char, 0) + 1
        
        res = -1

        for i in range(len(s)):
            if c[s[i]] == 1:
                res = i
                break
        
        return res