class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_i = len(a) - 1
        b_i = len(b) - 1
        rem = 0
        result = ""

        while a_i >= 0 or b_i >= 0:
            curSum = (int(a[a_i]) if a_i >= 0 else 0) + ((int(b[b_i]) if b_i >= 0 else 0)) + rem

            if curSum >= 2:
                result = str(curSum % 2) + result
                rem = 1
            else:
                result = str(curSum) + result
                rem = 0
            
            a_i -= 1
            b_i -= 1
        
        if rem > 0:
            result = str(rem) + result

        return result