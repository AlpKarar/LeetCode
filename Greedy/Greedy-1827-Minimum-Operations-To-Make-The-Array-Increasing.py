class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        
        res = 0

        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                cur = nums[i-1] - nums[i] + 1
                res += cur
                nums[i] += cur
        
        return res