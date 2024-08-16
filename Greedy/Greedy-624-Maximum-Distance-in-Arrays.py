class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        edge_points = []

        for i in range(len(arrays)):
            arr = arrays[i]

            if len(arr) > 1:
                edge_points += [(i, arr[0]), (i, arr[-1])]
            else:
                edge_points += [(i, arr[0])]
        
        edge_points = sorted(edge_points, key = lambda item: item[1])

        l = 0
        r = len(edge_points) - 1

        while l < r and edge_points[l][0] == edge_points[r][0]:
            if edge_points[r - 1][1] - edge_points[l][1] > edge_points[r][1] - edge_points[l + 1][1]:
                r -= 1
            else:
                l += 1

        return edge_points[r][1] - edge_points[l][1]