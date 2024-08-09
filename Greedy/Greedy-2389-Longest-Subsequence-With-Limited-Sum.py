class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums = sorted(nums)
        res = [0] * len(queries)

        for i in range(len(queries)):
            size = queries[i]
            sm = 0
            nums_i = 0

            while nums_i < len(nums) and sm < size:
                sm += nums[nums_i]
                nums_i += 1
            
            if sm <= size:
                res[i] = nums_i
            else:
                res[i] = nums_i - 1

        return res