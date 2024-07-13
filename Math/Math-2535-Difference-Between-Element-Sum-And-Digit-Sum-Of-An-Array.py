class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total = 0
        sum_digit = 0

        for num in nums:
            total += num

            while num > 0:
                sum_digit += num % 10
                num //= 10
        
        return abs(total - sum_digit)