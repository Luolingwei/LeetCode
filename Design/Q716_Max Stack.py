
'''
 when popmax, find from tail to head, pop and collect nums
 when curmax==element, the previous queue would not be affected
 push collected nums in reverse order to queue again.
'''

class MaxStack:

    def __init__(self):
        self.q = [(float('-inf'), float('-inf'))]

    def push(self, x: int) -> None:
        self.q.append((x, max(x, self.q[-1][1])))

    def pop(self) -> int:
        return self.q.pop()[0]

    def top(self) -> int:
        return self.q[-1][0]

    def peekMax(self) -> int:
        return self.q[-1][1]

    def popMax(self) -> int:
        curmax=self.q[-1][1]
        memo=[]
        while self.q[-1][0]!=curmax:
            memo.append(self.q.pop()[0])
        self.q.pop()
        for n in memo[::-1]:
            self.push(n)


stack=MaxStack()
stack.push(5)
stack.push(1)
stack.push(5)
print(stack.top())
print(stack.popMax())
print(stack.top())
print(stack.peekMax())
print(stack.pop())
print(stack.top())