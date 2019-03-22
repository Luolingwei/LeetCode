class MinStack:
    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(x)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[(float('inf'),float('inf'))]
    def push(self, x: int) -> None:
        self.stack.append((x,min(x,self.stack[-1][1])))
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
    def top(self) -> int:
        return self.stack[-1][0]
    def getMin(self) -> int:
        return self.stack[-1][1]

a=MinStack()
a.push(-2)
a.push(0)
a.push(-3)
a.getMin()
a.pop()
a.top()
a.getMin()