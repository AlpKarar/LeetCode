class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = {bill: 0 for bill in [5, 10, 20]}

        for bill in bills:
            if bill == 5:
                counts[5] += 1
            elif bill == 10:
                if counts[5] <= 0:
                    return False
                
                counts[10] += 1
                counts[5] -= 1
            else:
                if (counts[10] <= 0 and counts[5] < 3) or counts[5] <= 0:
                    return False
                
                counts[20] += 1
                
                if counts[10] >= 1:
                    counts[10] -= 1
                    counts[5] -= 1
                else:
                    counts[5] -= 3
        
        return True