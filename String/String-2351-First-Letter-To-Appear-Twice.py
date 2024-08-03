class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visited = set()
        res = ""

        for char in s:
            if char in visited:
                res = char

                break
            
            visited.add(char)

        return res