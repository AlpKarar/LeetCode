class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []

        while num > 0:
            curDigit = num % 10
            digits.append(curDigit)
            num = (num - curDigit) // 10
        
        digits = sorted(digits)
        l = 0
        r = len(digits) - 1
        res = 0

        while l < r:
            res += int(str(digits[l]) + str(digits[r]))
            l += 1
            r -= 1

        return res