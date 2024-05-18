class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        res = [0, 0]
        cur = 0

        for letter in s:
            temp = cur + widths[ord(letter) - ord("a")]

            if temp >= 100:
                res[0] += 1
                cur = widths[ord(letter) - ord("a")] if temp > 100 else 0
            else:
                cur += widths[ord(letter) - ord("a")]
        
        res[0] = res[0] + 1 if cur > 0 else res[0]
        res[1] = cur if cur > 0 else 100
 
        return res