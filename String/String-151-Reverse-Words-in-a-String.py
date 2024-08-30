class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        cur_word = ""

        for char in s:
            if char == " ":
                if cur_word != "":
                    words.append(cur_word)
                
                cur_word = ""
            else:
                cur_word += char
        
        if cur_word != "":
            words.append(cur_word)
        
        res = ""

        for i in range(len(words) - 1, -1 ,-1):
            res += words[i]

            if i > 0:
                res += " "
        
        return res