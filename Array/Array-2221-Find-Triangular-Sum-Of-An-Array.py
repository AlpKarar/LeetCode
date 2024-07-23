class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        while len(nums) > 1:
            n = len(nums) - 1
            t_nums = [0] * n

            for i in range(n):
                t_nums[i] = (nums[i] + nums[i+1]) % 10

            nums = t_nums

        return nums[0]