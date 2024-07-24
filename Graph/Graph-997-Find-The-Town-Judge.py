class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        trusteds = dict()
        town_judges = {i + 1 for i in range(n)}

        for rel in trust:
            trusteds[rel[1]] = trusteds.get(rel[1], []) + [rel[0]]
            trusteds[rel[0]] = trusteds.get(rel[0], [])

            if rel[0] in town_judges:
                town_judges.remove(rel[0])
        
        for trusted in trusteds:
            if len(trusteds[trusted]) == n - 1 and trusted in town_judges:
                return trusted
        
        return -1