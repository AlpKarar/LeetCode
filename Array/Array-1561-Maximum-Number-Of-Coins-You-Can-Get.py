class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)[::-1]
        i = 1
        j = len(piles) - 1
        res = 0

        while i < j:
            res += sorted_piles[i]
            i += 2
            j -= 1
        
        return res