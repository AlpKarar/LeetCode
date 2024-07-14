class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        i = n
        possible_places = 2 * n

        while i > 1:
            res *= (possible_places - 1) * possible_places // 2
            possible_places -= 2
            i -= 1
        
        return res % (10 ** 9 + 7)