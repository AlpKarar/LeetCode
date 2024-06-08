class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words = sorted(words, key = lambda word: int(word[-1]))
        
        for i in range(len(words)):
            words[i] = words[i][:-1]
        
        return " ".join(words)