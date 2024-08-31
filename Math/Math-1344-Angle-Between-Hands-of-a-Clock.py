class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_pos = 30 * (hour % 12 + minutes / 60)
        min_pos = minutes * 6
        res1 = abs(min_pos - hour_pos)
        res2 = 360 - res1

        return min(res1, res2)