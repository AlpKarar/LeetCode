class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checkSpeed(mid):
            total = 0

            for _, pile in enumerate(piles):
                if pile % mid != 0:
                    total += pile // mid + 1
                else:
                    total += pile // mid
            
            if total <= h:
                return True
            
            return False

        l = 1
        r = max(piles)

        while l < r:
            k = l + (r - l) // 2

            if checkSpeed(k):
                r = k
            else:
                l = k + 1
        
        return r