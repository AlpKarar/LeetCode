class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        res = [[0] * n for _ in range(m)]
        
        for i in range(m - 1, -1, -1):
            cur = []
            i_temp = i
            j = n - 1

            while i_temp >= 0 and j >= 0:
                cur.append((i_temp, j))
                i_temp -= 1
                j -= 1
            
            cur = sorted(cur, key = lambda x: mat[x[0]][x[1]])
            i_temp = i
            j = n - 1
            k = len(cur) - 1

            while k >= 0:
                res[i_temp][j] = mat[cur[k][0]][cur[k][1]]
                i_temp -= 1
                j -= 1
                k -= 1

        for j in range(n - 1, -1, -1):
            cur = []
            j_temp = j
            i = len(mat) - 1

            while j_temp >= 0 and i >= 0:
                cur.append((i, j_temp))
                j_temp -= 1
                i -= 1
            
            cur = sorted(cur, key = lambda x: mat[x[0]][x[1]])
            j_temp = j
            i = m - 1
            k = len(cur) - 1

            while k >= 0:
                res[i][j_temp] = mat[cur[k][0]][cur[k][1]]
                j_temp -= 1
                i -= 1
                k -= 1
        
        return res