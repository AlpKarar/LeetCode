class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = dict()
        dic2 = dict()

        for num in nums1:
            dic1[num] = dic1.get(num, 0) + 1
        
        for num in nums2:
            dic2[num] = dic2.get(num, 0) + 1

        
        res = []

        for num in dic1:
            if num in dic2:
                res += min(dic1[num], dic2[num]) * [num]
        
        return res        