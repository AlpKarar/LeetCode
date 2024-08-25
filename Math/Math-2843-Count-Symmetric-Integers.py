class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        if high < 10:
            return 0
        
        if low < 10:
            low = 10
        
        res = 0

        for num in range(low, high + 1):
            num_str = str(num)
            has_odd_length = True
            half = len(num_str) // 2

            if has_odd_length and num_str[:half] == num_str[half + 1:]:
                continue

            if len(num_str) % 2 == 0:
                has_odd_length = False
        
            half1_sum = sum([int(digit) for digit in num_str[:half]])
            half2_sum = sum([int(digit) for digit in num_str[half + 1 if has_odd_length else half:]])

            if half1_sum == half2_sum:
                res += 1
        
        return res