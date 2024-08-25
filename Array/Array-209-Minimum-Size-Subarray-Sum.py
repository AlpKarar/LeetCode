class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        start = 0
        temp_sum = nums[0]
        n = len(nums)
        res = n if temp_sum < target else 1

        for end in range(1, n):
            while temp_sum + nums[end] >= target:
                res = min(res, end - start + 1)
                temp_sum -= nums[start]
                start += 1
            
            temp_sum += nums[end]
        
        return res