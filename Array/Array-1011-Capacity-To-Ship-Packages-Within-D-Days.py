class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_cap = sum(weights)
        min_cap = max(weights)

        while min_cap < max_cap:
            cur_cap = min_cap + (max_cap - min_cap) // 2
            cur = 0
            n = 1
            
            for i in range(len(weights)):
                if cur + weights[i] > cur_cap:
                    n += 1
                    cur = 0
                
                cur += weights[i]
            
            if n > days:
                min_cap = cur_cap + 1
            else:
                max_cap = cur_cap
        
        return min_cap