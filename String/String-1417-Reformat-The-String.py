class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []

        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                letters.append(char)
        
        n = len(letters)
        m = len(digits)
        
        if abs(n - m) > 1:
            return ""
        
        i = 0
        res = ""

        while i < n and i < m:
            res += letters[i] + digits[i] if n > m else digits[i] + letters[i]
            i += 1
        
        while i < n:
            res += letters[i]
            i += 1
        
        while i < m:
            res += digits[i]
            i += 1

        return res