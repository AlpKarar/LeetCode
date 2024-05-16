class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weaks = []

        for i in range(len(mat)):
            weaks.append((sum(mat[i]), i))
        
        weaks = sorted(weaks, key = lambda x: x[0])

        return [weaks[i][1] for i in range(k)]