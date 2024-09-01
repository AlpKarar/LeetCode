class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ln = len(original)

        if ln != m * n:
            return []

        res = [[0] * n for _ in range(m)]

        for i in range(ln):
            res[i // n][i % n] = original[i]
        
        return res