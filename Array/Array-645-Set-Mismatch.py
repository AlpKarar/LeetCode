class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = {i : 0 for i in range(1, len(nums) + 1)}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        miss = 0
        dup = 0

        for num in count:
            if count[num] > 1:
                dup = num
            elif count[num] == 0:
                miss = num
            
            if dup > 0 and miss > 0:
                break
        
        return [dup, miss]