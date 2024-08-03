from collections import Counter

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter_t = Counter(target)
        counter_arr = Counter(arr)

        return counter_t == counter_arr