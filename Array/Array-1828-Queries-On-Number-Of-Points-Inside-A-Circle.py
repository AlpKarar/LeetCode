import math

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        
        for query in queries:
            circle_x = query[0]
            circle_y = query[1]
            r = query[2]
            num_of_points = 0

            for point in points:
                x = point[0]
                y = point[1]

                d1 = x - circle_x
                d2 = y - circle_y
                d = math.sqrt(d1 * d1 + d2 * d2)

                if d <= r:
                    num_of_points += 1

            res.append(num_of_points)
        
        return res