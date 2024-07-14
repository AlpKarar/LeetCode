class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i = 0

        while i < len(s) - len(part) + 1:
            if s[i:i+len(part)] == part:
                s = s[:i] + s[i+len(part):]
                i = 0
            else:
                i += 1
        
        return s