class MinStack:

    def __init__(self):
        self.minVal = []
        self.stack = []
        

    def push(self, val: int) -> None:
        if self.stack and self.minVal[-1] < val:
            self.minVal.append(self.minVal[-1])
        else:
            self.minVal.append(val)
        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minVal.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal[-1]
        
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()