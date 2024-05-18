class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexes = []

        for i in range(len(s)):
            if s[i] == c:
                indexes.append(i)
        
        res = [0] * len(s)
        j = 0

        for i in range(len(s)):
            if j == 0:
                if indexes[j] == i:
                    j += 1
                else:
                    res[i] = abs(indexes[j] - i)
            elif j < len(indexes):
                if indexes[j] == i:
                    j += 1
                else:
                    res[i] = min(abs(indexes[j] - i), abs(indexes[j-1] - i))
            else:
                res[i] = abs(indexes[j-1] - i)
        
        return res