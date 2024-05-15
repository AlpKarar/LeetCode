class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = [nums[0]]
        res = 1

        for i in range(1, len(nums)):
            if nums[i] != temp[-1]:
                temp.append(nums[i])
                res += 1
        
        for i in range(len(temp)):
            nums[i] = temp[i]
        
        return res