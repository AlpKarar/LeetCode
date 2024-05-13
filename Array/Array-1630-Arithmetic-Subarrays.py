class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = [True] * len(l)

        for i in range(len(l)):
            sorted_part = sorted(nums[l[i]:r[i] + 1])
            diff = sorted_part[1] - sorted_part[0]

            for j in range(1, len(sorted_part) - 1):
                curDiff = sorted_part[j+1] - sorted_part[j]

                if curDiff != diff:
                    res[i] = False
                    break
        
        return res