class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ")":
                stack.append(char)
            else:
                substring = []
                popChar = stack.pop()

                while popChar != "(":
                    substring.append(popChar[::-1] if len(popChar) > 1 else popChar)
                    popChar = stack.pop()
                
                stack += substring
        
        return "".join(stack)