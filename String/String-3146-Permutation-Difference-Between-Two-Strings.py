class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dict_s = {s[i]: i for i in range(len(s))}
        dict_t = {t[i]: i for i in range(len(t))}
        res = 0

        for char in s:
            res += abs(dict_s[char] - dict_t[char])
        
        return res