class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr = sorted(arr)

        for i in range(len(arr)):
            start = i + 1 if arr[i] >= 0 else 0
            end = len(arr) - 1 if arr[i] >= 0 else i - 1

            while start <= end:
                m = start + (end - start) // 2

                if arr[m] == 2 * arr[i]:
                    return True
                
                if arr[m] > 2 * arr[i]:
                    end = m - 1
                else:
                    start = m + 1
               
        return False