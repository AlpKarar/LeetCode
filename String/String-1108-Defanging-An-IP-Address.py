class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""

        for char in address:
            res += f"[{char}]" if char == "." else char
        
        return res