class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        start = 0
        maxSum = -sys.maxsize
        curSum = 0

        for end in range(len(nums)):
            curSum += nums[end]

            maxSum = max(maxSum, curSum)

            while curSum < 0:
                curSum -= nums[start]
                start += 1
        
        return maxSum