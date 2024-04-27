class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set()

        for jewel in jewels:
            jewels_set.add(jewel)
        
        res = 0

        for stone in stones:
            res += 1 if stone in jewels_set else 0
        
        return res