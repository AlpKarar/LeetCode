class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a_area = abs(ax1 - ax2) * abs(ay1 - ay2)
        b_area = abs(bx1 - bx2) * abs(by1 - by2)

        if bx1 > ax2 or ax1 > bx2 or ay1 > by2 or by1 > ay2:
            return a_area + b_area
        
        x = sorted([ax1, ax2, bx1, bx2])
        y = sorted([ay1, ay2, by1, by2])
       
        intersected_area = abs(x[2] - x[1]) * abs(y[2] - y[1])

        return a_area + b_area - intersected_area