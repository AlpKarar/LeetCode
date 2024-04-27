class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        i = 0

        if ruleKey == "color":
            i = 1
        elif ruleKey == "name":
            i = 2
        
        res = 0

        for item in items:
            if item[i] == ruleValue:
                res += 1
        
        return res