class Solution:
    def countDigits(self, num: int) -> int:
        count = dict()

        for digit_str in str(num):
            count[int(digit_str)] = count.get(int(digit_str), 0) + 1
        
        res = 0

        for digit in count:
            if num % digit == 0:
                res += count[digit]
        
        return res