class CustomStack:

    def __init__(self, maxSize: int):
        self.capacity = maxSize
        self.length = 0
        self.stack = []
        

    def push(self, x: int) -> None:
        if self.length >= self.capacity:
            return
        
        self.stack.append(x)
        self.length += 1
        

    def pop(self) -> int:
        if self.length <= 0:
            return -1
        
        self.length -= 1

        return self.stack.pop()
        

    def increment(self, k: int, val: int) -> None:
        for i in range(self.length if k >= self.length else k):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)