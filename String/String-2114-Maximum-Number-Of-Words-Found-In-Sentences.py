class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0

        for sentence in sentences:
            count = 1

            for char in sentence:
                if char == " ":
                    count += 1
            
            res = max(res, count)
        
        return res