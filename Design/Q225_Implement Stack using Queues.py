
# 往非空的一个queue中push，pop时把非空队列往空队列中转，剩一个元素，pop出此元素，后进先出

from collections import deque
class MyStack:

    def __init__(self):
        self.q1, self.q2 = deque(), deque()

    def push(self, x: int) -> None:
        if self.q1:
            self.q1.append(x)
        else:
            self.q2.append(x)

    def pop(self) -> int:
        if not self.q1:
            while len(self.q2) > 1:
                self.q1.append(self.q2.popleft())
            return self.q2.popleft()
        else:
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            return self.q1.popleft()

    def top(self) -> int:
        if self.q1:
            return self.q1[-1]
        else:
            return self.q2[-1]

    def empty(self) -> bool:
        return not self.q1 and not self.q2