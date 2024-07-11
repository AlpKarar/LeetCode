class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []

        while n > 0:
            digits.append(n % 10)
            n //= 10
        
        sm = 0
        product = 1

        for digit in digits:
            sm += digit
            product *= digit
        
        return product - sm