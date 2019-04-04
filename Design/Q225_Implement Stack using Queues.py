class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1,self.queue2=[],[]

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.insert(0,x)
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

        while len(self.queue1)>1:
            self.queue2.insert(0,self.queue1.pop())
        num=self.queue1.pop()
        while self.queue2:
            self.queue1.insert(0,self.queue2.pop())
        return num

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()