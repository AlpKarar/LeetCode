class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1 = {char for char in "qwertyuiop"}
        row2 = {char for char in "asdfghjkl"}
        row3 = {char for char in "zxcvbnm"}

        res = []

        for word in words:
            row = row1

            if word[0].lower() in row2:
                row = row2
            elif word[0].lower() in row3:
                row = row3
            
            isBreak = False

            for i in range(1, len(word)):
                if word[i].lower() not in row:
                    isBreak = True
                    break
            
            if not isBreak:
                res.append(word)
        
        return res