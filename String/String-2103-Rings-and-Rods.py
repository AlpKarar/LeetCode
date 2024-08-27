class Solution:
    def countPoints(self, rings: str) -> int:
        
        count = dict()
        visited = set()
        res = 0

        for i in range(0, len(rings) - 1, 2):
            count[rings[i + 1]] = count.get(rings[i + 1], set())
            count[rings[i + 1]].add(rings[i])

            if len(count[rings[i + 1]]) == 3 and rings[i + 1] not in visited:
                res += 1
                visited.add(rings[i + 1])

        return res