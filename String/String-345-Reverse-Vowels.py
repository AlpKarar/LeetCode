class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"

        s_list = [char for char in s]
        l = 0
        r = len(s) - 1

        while l < r:
            if s_list[l] not in vowels:
                l += 1
                continue
            
            if s_list[r] not in vowels:
                r -= 1
                continue
            
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1

        return "".join(s_list)

# Beats 97.40%