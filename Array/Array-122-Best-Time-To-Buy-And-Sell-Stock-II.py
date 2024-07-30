class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        curMax = 0
        res = 0

        for i in range(1, len(prices)):
            if prices[i] <= prices[start]:
                if curMax > 0:
                    res += curMax
                
                start = i
                curMax = 0
            elif prices[i] - prices[start] >= curMax:
                curMax = prices[i] - prices[start]
            else:
                res += curMax
                curMax = 0
                start = i

        if curMax > 0:
            res += curMax

        return res