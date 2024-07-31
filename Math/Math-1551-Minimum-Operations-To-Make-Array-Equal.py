class Solution:
    def minOperations(self, n: int) -> int:
        total = n ** 2
        item = total // n
        max_diff = item - 1
        n_new = 0
        res = 0
        
        if max_diff % 2 == 0:
            n_new = max_diff // 2 + 1
            res = n_new ** 2 - n_new
        else:
            n_new = (max_diff - 1) // 2 + 1
            res = n_new ** 2
        
        return res