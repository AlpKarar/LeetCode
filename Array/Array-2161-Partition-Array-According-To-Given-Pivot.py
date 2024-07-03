class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        p = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                p.append(num)
            else:
                greater.append(num)
        
        return less + p + greater