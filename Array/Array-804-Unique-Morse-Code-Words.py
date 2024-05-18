class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()

        for word in words:
            cur = ""

            for letter in word:
                cur += morse[ord(letter) - ord("a")]
            
            res.add(cur)

        return len(res)