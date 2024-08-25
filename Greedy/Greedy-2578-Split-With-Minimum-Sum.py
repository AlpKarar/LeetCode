class Solution:
    def splitNum(self, num: int) -> int:
        num_str = sorted([digit for digit in str(num)])
        n = len(num_str)
        a = ""
        b = ""

        for i in range(n):
            if i % 2 == 0:
                a += num_str[i]
            else:
                b += num_str[i]
        
        return int(a) + int(b)