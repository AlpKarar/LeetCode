class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []
        
        for char in s:
            if not char in match:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                
                if match[char] != stack[-1]:
                    return False
                
                stack.pop()
        
        if len(stack) > 0:
            return False
        
        return True
