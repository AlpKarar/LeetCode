class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = dict()
        max_freq = 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            max_freq = max(max_freq, freq[num])
        
        freq_arr = [[] for _ in range(max_freq)]
        
        for num in freq:
            freq_arr[freq[num] - 1] += [num] * freq[num]
        
        res = []

        for sub_freq_nums in freq_arr:
            if sub_freq_nums:
                res += sorted(sub_freq_nums)[::-1]
        
        return res