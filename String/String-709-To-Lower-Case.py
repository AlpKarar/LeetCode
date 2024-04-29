class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""

        for char in s:
            res += chr(ord(char) + 32) if char.isupper() else char
        
        return res