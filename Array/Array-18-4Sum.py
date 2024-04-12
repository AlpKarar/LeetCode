class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = list()

        nums = sorted(nums)

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if i + 1 < j and nums[j] == nums[j-1]:
                    continue
                                            
                l = j + 1
                r = len(nums) - 1

                while l < r:
                    curSum = nums[i] + nums[j] + nums[l] + nums[r]

                    if curSum == target:
                        result.append((nums[i], nums[j], nums[l], nums[r]))

                        while l < r and nums[l] == nums[l+1]:
                            l += 1

                        while l < r and nums[r] == nums[r-1]:
                            r -= 1

                        l += 1
                        r -= 1
                    elif curSum > target:
                        r -= 1
                    else:
                        l += 1
        
        return result