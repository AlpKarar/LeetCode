class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = dict()

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        count_t = dict()

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        res = ""

        for char in t:
            if char not in s:
                res += char
                break
            
            if count_s[char] != count_t[char]:
                res += abs(count_s[char] - count_t[char]) * char
                break
        
        return res