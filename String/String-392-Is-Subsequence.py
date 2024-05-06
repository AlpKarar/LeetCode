class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s):
            while j < len(t) and s[i] != t[j]:
                j += 1

            if j == len(t):
                return False
            
            i += 1
            j += 1
        
        return True