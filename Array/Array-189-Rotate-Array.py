class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k %= len(nums)

        rotated_nums = nums[-k:]

        for i in range(len(nums) - 1 - k, -1, -1):
            nums[i + k] = nums[i]
            
        for i in range(len(rotated_nums)):
            nums[i] = rotated_nums[i]