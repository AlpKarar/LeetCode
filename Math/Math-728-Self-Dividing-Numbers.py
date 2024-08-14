class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for num in range(left, right + 1):
            temp = num
            isBreak = False

            while temp > 0:
                last_digit = temp % 10

                if last_digit == 0 or num % last_digit != 0:
                    isBreak = True
                    break
                
                temp //= 10
            
            if not isBreak:
                res.append(num)
        
        return res