class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = dict()

        for string in strs:
            sortedString = "".join(sorted(string))

            s[sortedString] = s.get(sortedString, []) + [string]
        
        return s.values()