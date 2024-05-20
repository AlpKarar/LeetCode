class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums) 
        res = 0

        for i in range(n - 1):
            if i == 0 or nums[i] != nums[i-1]:
                l = i + 1
                r = n - 1

                while l <= r:
                    m = l + (r - l) // 2

                    if nums[m] == nums[i] + k:
                        res += 1
                        break

                    if nums[m] < nums[i] + k:
                        l = m + 1
                    else:
                        r = m - 1
        
        return res