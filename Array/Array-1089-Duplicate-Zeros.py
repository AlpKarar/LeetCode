class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        i = 0

        while i < len(arr):
            if arr[i] == 0 and i + 1 < len(arr):
                arr[i + 2:] = arr[i + 1:-1]
                arr[i + 1] = 0
                i += 1
            
            i += 1