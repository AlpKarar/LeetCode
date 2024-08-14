class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0

        for substr in strs:
            res = max(res, int(substr) if substr.isdigit() else len(substr))
        
        return res