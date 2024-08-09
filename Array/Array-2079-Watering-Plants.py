class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        water = capacity

        for i in range(len(plants)):
            if plants[i] <= water:
                res += 1
                water -= plants[i]
            else:
                water = capacity - plants[i]
                res += 2 * i + 1
        
        return res