class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                if nums[l] == 0:
                    l = r
            elif nums[l] == 1:
                res = max(res, r - l)
                l = r
        
        if nums[-1] == 1:
            res = max(res, len(nums) - l)

        return res