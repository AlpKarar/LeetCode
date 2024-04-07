class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        if n == 2:
            return "11"
        
        if n == 3:
            return "21"
        
        res = "21"

        for _ in range(3, n):
            cur = ""
            count = 1
            for i in range(1, len(res)):
                if res[i] == res[i-1]:
                    count += 1
                else:
                    cur += str(count) + res[i-1]
                    count = 1
            
            cur += str(count) + res[-1]
            res = cur
        
        return res