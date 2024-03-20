class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_m = dict()
        t_visited = set()

        for i in range(len(s)):
            if s[i] in s_m:
                if t[i] != s_m[s[i]]:
                    return False
            else:
                if t[i] in t_visited:
                    return False
                
                s_m[s[i]] = t[i]
                t_visited.add(t[i])
        
        return True