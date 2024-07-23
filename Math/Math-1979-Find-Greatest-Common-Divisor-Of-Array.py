class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_num = nums[0]
        min_num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
            elif nums[i] < min_num:
                min_num = nums[i]
        
        res = min_num

        while not (max_num % res == 0 and min_num % res == 0):
            res -= 1
        
        return res