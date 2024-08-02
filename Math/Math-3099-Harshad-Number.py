class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sm = 0
        tmp = x

        while tmp > 0:
            sm += tmp % 10
            tmp //= 10
        
        if x % sm == 0:
            return sm
        
        return -1