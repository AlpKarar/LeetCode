class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        res = []
        l, r = 0, len(nums) - 1

        while l < r:
            res.append((nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        
        return sorted(res)[0]