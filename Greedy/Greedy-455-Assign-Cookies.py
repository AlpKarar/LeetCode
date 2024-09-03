class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)[::-1]
        s = sorted(s)[::-1]

        g_i = 0
        res = 0

        for s_i in range(len(s)):
            while g_i < len(g) and g[g_i] > s[s_i]:
                g_i += 1
            
            if g_i == len(g):
                return res
            
            res += 1
            g_i += 1
        
        return res