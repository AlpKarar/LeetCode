class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(curStr, l, r):
            if len(curStr) == 2 * n:
                result.append(curStr)
                return
            
            if l < n:
                helper(curStr + "(", l + 1, r)
            
            if r < l:
                helper(curStr + ")", l, r + 1)
        
        helper("", 0, 0)

        return result