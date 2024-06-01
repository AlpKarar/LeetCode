class Solution:
    def partitionString(self, s: str) -> int:
        visited = set()
        res = 0

        for char in s:
            if char in visited:
                res += 1
                visited = set()
            
            visited.add(char)
        
        return res + 1