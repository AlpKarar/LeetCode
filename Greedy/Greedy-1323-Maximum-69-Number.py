class Solution:
    def maximum69Number (self, num: int) -> int:
        res = ""
        isFirst6 = True

        for digit in str(num):
            if digit == "6" and isFirst6:
                res += "9"
                isFirst6 = False
            else:
                res += digit
        
        return int(res)