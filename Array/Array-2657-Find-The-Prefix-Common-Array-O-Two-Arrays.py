class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        set_A = set()
        set_B = set()
        res = [0] * n
        
        for i in range(n):            
            if i > 0:
                res[i] = res[i-1]

            set_A.add(A[i])
            set_B.add(B[i])

            if A[i] == B[i]:
                res[i] += 1
                continue
           
            if A[i] in set_A and A[i] in set_B:
                res[i] += 1
            
            if B[i] in set_A and B[i] in set_B:
                res[i] += 1
        
        return res