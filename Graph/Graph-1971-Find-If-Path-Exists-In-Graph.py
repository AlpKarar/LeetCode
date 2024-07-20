class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        arr = [None] * n

        for edge in edges:
            if not arr[edge[1]]:
                arr[edge[1]] = [edge[0]]
            else:
                arr[edge[1]].append(edge[0])
            
            if not arr[edge[0]]:
                arr[edge[0]] = [edge[1]]
            else:
                arr[edge[0]].append(edge[1])            

        visited = set()
        cur_parents = [destination]

        while cur_parents:
            cur = cur_parents.pop()

            if cur == source:
                return True
            
            visited.add(cur)

            if arr[cur]:
                for parent in arr[cur]:
                    if parent not in visited:
                        cur_parents.append(parent)
        
        return False