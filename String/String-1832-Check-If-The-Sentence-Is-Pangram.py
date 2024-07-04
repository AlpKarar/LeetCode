class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        letters = set()

        for letter in alphabet:
            letters.add(letter)
        
        for char in sentence:
            if char in letters:
                letters.remove(char)
        
        return len(letters) == 0