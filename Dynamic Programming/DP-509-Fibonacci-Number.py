class Solution:
    def fib(self, n: int) -> int:
        storage = dict()

        def helper(n):
            if n in storage:
                return storage[n]
            
            if n == 1:
                return 1
            
            if n < 1:
                return 0
            
            newVal = helper(n - 1) + helper(n - 2)
            storage[n] = newVal

            return newVal
        
        return helper(n)