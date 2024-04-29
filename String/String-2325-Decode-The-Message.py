class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alph = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        subs = dict()

        for char in key:
            if char == " ":
                continue
            
            if char in subs:
                continue
            
            subs[char] = alph[i]
            i += 1
        
        res = ""

        for char in message:
            res += subs[char] if char in subs else char
        
        return res