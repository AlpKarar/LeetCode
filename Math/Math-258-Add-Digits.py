class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        
        while res // 10 > 0:
            cur = 0

            while res > 0:
                cur += res % 10
                res //= 10
            
            res = cur
        
        return res