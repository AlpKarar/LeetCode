class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        res = ["a"] * len(s)
        l = 0
        r = len(s) - 1

        while l <= r:
            if ord(s[l]) > ord(s[r]):
                res[l] = s[r]
                res[r] = s[r]
            else:
                res[l] = s[l]
                res[r] = s[l]
            
            l += 1
            r -= 1
        
        return "".join(res)