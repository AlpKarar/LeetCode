class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices = set(edge[0] for edge in edges)

        for edge in edges:
            if edge[1] in vertices:
                vertices.remove(edge[1])
        
        return vertices