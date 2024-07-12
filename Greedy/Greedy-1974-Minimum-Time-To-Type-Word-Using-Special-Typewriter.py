class Solution:
    def minTimeToType(self, word: str) -> int:
        word = "a" + word
        res = 0

        for i in range(1, len(word)):
            diff1 = ord("z") - ord(word[i - 1]) + 1 + ord(word[i]) - ord("a")
            diff2 = abs(ord(word[i]) - ord(word[i-1]))
            diff3 = ord(word[i - 1]) - ord("a") + 1 + ord("z") - ord(word[i])

            if diff1 <= diff2 and diff1 <= diff3:
                res += diff1
            elif diff1 <= diff2:
                res += diff3
            elif diff1 <= diff3:
                res += diff2
            elif diff2 <= diff3:
                res += diff2
            else:
                res += diff3

            res += 1
        
        return res