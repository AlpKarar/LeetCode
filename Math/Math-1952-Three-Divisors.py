class Solution:
    def isThree(self, n: int) -> bool:
        i = n // 2
        count = 1

        while i > 0:
            if n % i == 0:
                count += 1
            
            i -= 1
        
        return count == 3