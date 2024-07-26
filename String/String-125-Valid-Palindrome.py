class Solution:
    def isPalindrome(self, s: str) -> bool:   
        s = s.lower()
        i = 0
        lenS = len(s)

        while i < lenS:
            if not s[i].isalnum():
                s = s.replace(s[i], "")
                i -= 1
                lenS = len(s)
            
            i += 1
        
        return s == s[::-1]