class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        i = 0

        while i < k:
            if numOnes > 0:
                numOnes -= 1
                res += 1
            elif numZeros > 0:
                numZeros -= 1
            else:
                numNegOnes -= 1
                res -= 1

            i += 1

        return res