class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        vowels_s = []

        for char in s:
            if char in vowels:
                vowels_s.append(char)
        
        sorted_vowels_s = sorted(vowels_s)

        res = ""
        i = 0

        for char in s:
            if char in vowels:
                res += str(sorted_vowels_s[i])
                i += 1
            else:
                res += char
        
        return res