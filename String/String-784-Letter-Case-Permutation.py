class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def helper(i, cur):
            if i == len(s):
                res.append(cur)
                return
            
            if s[i].isdigit():
                helper(i + 1, cur + s[i])
            else:
                helper(i + 1, cur + s[i].lower())
                helper(i + 1, cur + s[i].upper())

        helper(0, "")

        return res