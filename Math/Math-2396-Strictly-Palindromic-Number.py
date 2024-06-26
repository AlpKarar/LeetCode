class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        def helper(num, base):
            res = ""

            while num > 0:
                res = str(num % base) + res
                num //= base
        
            return res
        
        for base in range(2, n - 1):
            num = helper(n, base)

            if num != num[::-1]:
                return False
        
        return True