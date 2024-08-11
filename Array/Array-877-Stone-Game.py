class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice = 0
        bob = 0
        i = 0

        while piles:
            if i == 0:
                if piles[0] > piles[-1]:
                    alice += piles[0]
                    piles = piles[1:]
                else:
                    alice += piles[-1]
                    piles = piles[:-1]
                
                i = 1
            else:
                if len(piles) == 1 or piles[0] < piles[-1]:
                    bob += piles[0]
                    piles = piles[1:]
                else:
                    bob += piles[-1]
                    piles = piles[:-1]

                i = 0
        
        return alice > bob