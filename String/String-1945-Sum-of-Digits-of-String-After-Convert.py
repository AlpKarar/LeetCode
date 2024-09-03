class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s_num = ""

        for char in s:
            s_num += str(ord(char) - ord("a") + 1)
        
        res = 0

        for _ in range(k):
            res = 0
            
            for char in s_num:
                res += int(char)
            
            s_num = str(res)
        
        return res