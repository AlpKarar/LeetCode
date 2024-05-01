class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_count = dict()
        res = 0

        for i in range(len(nums)):
            num_count[nums[i]] = num_count.get(nums[i], 0 ) + 1
        
        for count in num_count.values():
            res += count * (count - 1) // 2
        
        return res