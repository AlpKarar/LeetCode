class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        res = 0

        for subLen in range(1, len(arr) + 1, 2):
            for i in range(len(arr) - subLen + 1):
                res += sum(arr[i:i + subLen])

        return res