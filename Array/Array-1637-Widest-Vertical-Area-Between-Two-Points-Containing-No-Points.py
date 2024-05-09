class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points_sorted = sorted(points, key = lambda x: x[0])
        res = 0

        for i in range(1, len(points_sorted)):
            res = max(res, points_sorted[i][0] - points_sorted[i-1][0])
        
        return res