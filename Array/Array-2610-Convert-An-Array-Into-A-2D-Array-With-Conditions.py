class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = dict()

        for num in nums:
            c[num] = c.get(num, 0) + 1
        
        res = []
        nums_set = set(nums)

        while nums_set:
            row = []

            for num in c:
                if num in nums_set:
                    row.append(num)
                    c[num] -= 1
                
                if c[num] == 0 and num in nums_set:
                    nums_set.remove(num)

            res.append(row)
        
        return res