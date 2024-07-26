class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        total = sum(nums)
        prev_sum = 0

        for i in range(len(nums) - 1, -1, -1):
            cur_sum = prev_sum + nums[i]

            if cur_sum > total - cur_sum:
                return nums[i:][::-1]
            
            prev_sum = cur_sum
        
        return nums