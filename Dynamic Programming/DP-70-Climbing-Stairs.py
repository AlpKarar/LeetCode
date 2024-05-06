class Solution:
    def climbStairs(self, n: int) -> int:
        num_steps = dict()

        def helper(i):
            if i in num_steps:
                return num_steps[i]
            
            if i == n:
                return 1
            
            if i > n:
                return 0

            curNumOfSteps = helper(i + 1) + helper(i + 2)

            num_steps[i] = curNumOfSteps

            return curNumOfSteps

        return helper(0)