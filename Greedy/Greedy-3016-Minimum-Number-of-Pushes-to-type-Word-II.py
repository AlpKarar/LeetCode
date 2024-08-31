class Solution:
    def minimumPushes(self, word: str) -> int:
        c = dict()

        for char in word:
            c[char] = c.get(char, 0) + 1
        
        pairs = []

        for char in c:
            pairs.append((char, c[char]))
        
        n = len(pairs)
        
        pairs = sorted(pairs, key = lambda pair: pair[1])[::-1]

        res = 0

        for i in range(n):
            res += (i // 8 + 1) * pairs[i][1]
        
        return res