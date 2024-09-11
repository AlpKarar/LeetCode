from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        sorted_items = sorted(count.items(), key = lambda item: item[1])[::-1]

        res = ""

        for char, val in sorted_items:
            res += char * val
        
        return res