class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set([char for char in allowed])
        res = 0

        for word in words:
            isBreak = False

            for char in word:
                if char not in allowed_set:
                    isBreak = True
                    break
            
            if not isBreak:
                res += 1
        
        return res