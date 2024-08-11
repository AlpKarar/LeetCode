class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        full = numBottles
        empty = 0

        while full > 0:
            res += full
            empty += full
            full = empty // numExchange
            empty %= numExchange
        
        return res