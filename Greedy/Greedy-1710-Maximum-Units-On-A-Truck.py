class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda item: item[1])[::-1]

        cur = 0
        res = 0

        for item in boxTypes:
            if cur >= truckSize:
                break
            
            if cur + item[0] >= truckSize:
                res += (truckSize - cur) * item[1]
            else:
                res += item[0] * item[1]
            
            cur += item[0]
        
        return res