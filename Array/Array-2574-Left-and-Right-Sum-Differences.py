class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n

        for i in range(n - 1):
            leftSum[i + 1] = leftSum[i] + nums[i]
            rightSum[n - 2 - i] = rightSum[n - 1 - i] + nums[n - 1 - i]

        res = [0] * n

        for i in range(n):
            res[i] = abs(leftSum[i] - rightSum[i])
        
        return res