class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)

        l = 0
        r = len(nums)

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > m:
                r = m
            else:
                l = m + 1
        
        return l