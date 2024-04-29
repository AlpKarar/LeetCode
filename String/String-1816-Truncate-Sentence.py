class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res = ""
        count = 0
        i = 0

        while i < len(s):
            if s[i] == " ":
                count += 1
            
            if count == k:
                break

            res += s[i]
            i += 1
        
        return res