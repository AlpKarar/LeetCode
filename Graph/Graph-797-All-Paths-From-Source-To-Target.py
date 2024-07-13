class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        def dfs(cur, path):
            if cur == len(graph) - 1:
                path.append(cur)
                res.append(path.copy())
                return
            
            path.append(cur)

            for neighbour in graph[cur]:
                dfs(neighbour, path.copy())
        
        dfs(0, [])

        return res