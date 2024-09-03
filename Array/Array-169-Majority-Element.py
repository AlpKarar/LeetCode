class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = len(nums) / 2
        count = dict()

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        res = 0

        for num in count:
            if count[num] > half:
                res = num
                break
        
        return res