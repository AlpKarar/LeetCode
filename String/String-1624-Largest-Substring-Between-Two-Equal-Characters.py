class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_indexes = dict()
        res = -1

        for i in range(len(s)):
            if s[i] in char_indexes:
                res = max(res, i - char_indexes[s[i]] - 1)
            else:
                char_indexes[s[i]] = i
        
        return res