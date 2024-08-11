class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        res = 0

        for cost in costs:
            if coins >= cost:
                coins -= cost
                res += 1
        
        return res