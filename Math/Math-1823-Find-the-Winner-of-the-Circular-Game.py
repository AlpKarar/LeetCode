class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n + 1)]

        idx = k - 1

        while len(arr) > 1:
            arr = arr[:idx] + arr[idx + 1:]
            idx = (idx + k - 1) % len(arr)
        
        return arr[0]