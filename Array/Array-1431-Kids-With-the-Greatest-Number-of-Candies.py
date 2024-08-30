class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_cand = max(candies)
        
        return [True if candy + extraCandies >= max_cand else False for candy in candies]