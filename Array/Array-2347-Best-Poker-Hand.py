class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        
        c = dict()

        for rank in ranks:
            c[rank] = c.get(rank, 0) + 1

        set_c = set(c.values())

        if max(set_c) >= 3:
            return "Three of a Kind"
        
        if max(set_c) >= 2:
            return "Pair"
        
        return "High Card"