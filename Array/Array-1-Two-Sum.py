class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()
        result = [0, 0]

        for i in range(len(nums)):
            other = target - nums[i]

            if other in s:
                result[0] = s[other]
                result[1] = i
                break
            else:
                s[nums[i]] = i
        
        return result