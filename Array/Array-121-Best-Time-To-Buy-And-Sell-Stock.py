class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            elif prices[r] - prices[l] > res:
                res = prices[r] - prices[l]
            
            r += 1
        
        return res