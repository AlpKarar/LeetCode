class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [" " for _ in range(len(s))]

        for i in range(len(s)):
            arr[indices[i]] = s[i]
        
        return "".join(arr)