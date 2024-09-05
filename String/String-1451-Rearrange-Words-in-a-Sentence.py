class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        words = sorted(text.split(" "), key = lambda word: len(word))
        
        return " ".join(words).replace(words[0][0], words[0][0].upper(), 1)     