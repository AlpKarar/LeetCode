class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res = ""

        for word in words:
            l = 0
            r = len(word) - 1
            isPalindromic = True

            while l < r:
                if word[l] != word[r]:
                    isPalindromic = False
                    break
                
                l += 1
                r -= 1
            
            if isPalindromic:
                res = word
                break
        
        return res