class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums = sorted(nums)
        newNums = [0] * len(nums)
        newNums[0] = nums[0]
        res = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] or nums[i] <= newNums[i-1]:
                newNums[i] = newNums[i-1] + 1
                res += newNums[i] - nums[i]
            else:
                newNums[i] = nums[i]
        
        return res