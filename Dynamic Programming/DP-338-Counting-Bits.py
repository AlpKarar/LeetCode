class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        res = []

        for num in range(n + 1):
            cur = 0

            while num > 0:
                cur += num % 2                
                num //= 2
            
            res.append(cur)
        
        return res
        """

        res = [0] * (n + 1)

        for i in range(1, n + 1):
            res[i] = res[i//2] + i % 2
        
        return res