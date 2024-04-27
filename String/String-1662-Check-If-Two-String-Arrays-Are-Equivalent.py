class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        p1 = 0
        i1 = 0
        p2 = 0
        i2 = 0

        len_word1 = len(word1)
        len_word2 = len(word2)

        while i1 < len_word1 and i2 < len_word2:
            if word1[i1][p1] != word2[i2][p2]:
                return False
            
            if p1 + 1 == len(word1[i1]):
                p1 = 0
                i1 += 1
            else:
                p1 += 1

            if p2 + 1 == len(word2[i2]):
                p2 = 0
                i2 += 1
            else:
                p2 += 1

        if i1 == len_word1 and i2 == len_word2:
            return True
        
        return False