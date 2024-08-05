class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = dict()
        freq = dict()

        for item in arr:
            count[item] = count.get(item, 0) + 1
        
        for item in count:
            freq[count[item]] = freq.get(count[item], []) + [item]
        
        return freq[1][k-1] if 1 in freq and len(freq[1]) >= k else ""