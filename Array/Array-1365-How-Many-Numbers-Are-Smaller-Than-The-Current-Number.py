class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_indexed = [(i, nums[i]) for i in range(len(nums))]
        nums_indexed_sorted = sorted(nums_indexed, key = lambda x: x[1])
        res = [0] * len(nums)

        for j in range(1, len(nums_indexed_sorted)):
            if nums_indexed_sorted[j][1] == nums_indexed_sorted[j - 1][1]:
                res[nums_indexed_sorted[j][0]] = res[nums_indexed_sorted[j - 1][0]]
            else:
                res[nums_indexed_sorted[j][0]] = j
        
        return res