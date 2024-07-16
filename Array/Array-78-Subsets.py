class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        def helper(cur, rem, subLen):
            if len(cur) == subLen:
                res.append(cur.copy())
                return
            
            for i in range(len(rem)):
                temp = rem[i + 1:]
                cur.append(rem[i])
                helper(cur, temp, subLen)
                cur.pop()

        

        for subLen in range(1, len(nums) + 1):
            helper([], nums, subLen)
        
        return res