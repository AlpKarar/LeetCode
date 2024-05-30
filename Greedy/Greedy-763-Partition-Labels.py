class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indexes = {s[i]: i for i in range(len(s))}
        mx = 0
        size = 0
        res = []

        for i, char in enumerate(s):
            size += 1
            mx = max(mx, last_indexes[char])

            if  mx == i:
                res.append(size)
                size = 0
        
        return res