class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_count = dict()

        for letter in s:
            letter_count[letter] = letter_count.get(letter, 0) + 1
        
        res = 0
        isOdd = False

        for letter in letter_count:
            res += (letter_count[letter] if letter_count[letter] % 2 == 0 else letter_count[letter] - 1)
            
            if letter_count[letter] % 2 != 0:
                isOdd = True
        
        return res + 1 if isOdd else res