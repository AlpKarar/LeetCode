class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        res = 0

        for char in s:
            if len(stack) == 0:
                res += 1
                stack.append(char)
            elif char == stack[0]:
                stack.append(char)
            else:
                stack.pop()
        
        return res