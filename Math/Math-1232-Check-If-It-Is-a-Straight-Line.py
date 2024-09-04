class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        denominator = (coordinates[1][0] - coordinates[0][0])
        slope = (coordinates[1][1] - coordinates[0][1]) / denominator if denominator != 0 else float("-inf")

        for i in range(2, len(coordinates)):
            cur_denominator = (coordinates[i][0] - coordinates[i - 1][0])
            cur_slope = (coordinates[i][1] - coordinates[i - 1][1]) / cur_denominator if cur_denominator != 0 else float("-inf")

            if cur_slope != slope:
                return False
        
        return True