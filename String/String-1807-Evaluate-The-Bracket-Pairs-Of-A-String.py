class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        pairs = {item[0]: item[1] for item in knowledge}
        i = 0
        res = ""

        while i < len(s):
            if s[i] != "(":
                res += s[i]
            else:
                i += 1
                key = ""

                while s[i] != ")":
                    key += s[i]
                    i += 1
                
                res += pairs[key] if key in pairs else "?"
            
            i += 1
        
        return res