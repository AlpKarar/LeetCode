class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start = -1
        end = len(s) + 1
        res = []

        for char in s:
            if char == "D":
                end -= 1
                res.append(end)
            else:
                start += 1
                res.append(start)
        
        if s[-1] == "D":
            res.append(start + 1)
        else:
            res.append(end - 1)

        return res