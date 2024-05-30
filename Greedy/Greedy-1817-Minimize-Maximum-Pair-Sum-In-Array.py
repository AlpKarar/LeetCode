class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l, r = 0, len(nums) - 1
        res = 0

        while l < r:
            res = max(res, nums[l] + nums[r])
            l += 1
            r -= 1
        
        return res