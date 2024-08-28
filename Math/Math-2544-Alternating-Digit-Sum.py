class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        stack = []

        while n > 0:
            stack.append(n % 10)
            n //= 10
        
        i = 0
        res = 0

        while stack:
            res += stack.pop() * (1 if i % 2 == 0 else -1)
            i += 1
        
        return res