class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0

        while n >= k:
            res += n % k
            n //= k
        
        res += n

        return res