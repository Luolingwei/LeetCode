
# 先往stack1中push，pop的时候把stack1中的数全部转到stack2中，先进先出

class MyQueue:

    def __init__(self):
        self.stack1,self.stack2 =[],[]

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            return self.stack1[0]
        else:
            return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2