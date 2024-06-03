class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p_t = 0
        len_s = len(s)
        len_t = len(t)

        for i in range(len_s):
            if s[i] == t[p_t]:
                p_t += 1
            
            if p_t == len_t:
                break
        
        return len_t - p_t