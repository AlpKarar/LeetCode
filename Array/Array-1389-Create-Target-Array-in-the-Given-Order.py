class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = [nums[0]]

        for i in range(1, len(nums)):
            res = res[:index[i]] + [nums[i]] + res[index[i]:]
        
        return res