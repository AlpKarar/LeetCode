class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)

        return k * maxNum + (k * (k - 1)) // 2