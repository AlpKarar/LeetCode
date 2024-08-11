class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        keys = {0}

        while keys:
            key = keys.pop()
            visited.add(key)

            for newKey in rooms[key]:
                if newKey not in visited:
                    keys.add(newKey)
        
        return len(visited) == len(rooms)