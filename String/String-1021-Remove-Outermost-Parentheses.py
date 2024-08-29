class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = [s[0]]
        res = ""

        for i in range(1, len(s)):
            if s[i] == "(":
                if len(stack) > 0:
                    res += "("
                
                stack.append("(")
            else:
                if len(stack) > 1:
                    res += ")"
                
                stack.pop()
        
        return res