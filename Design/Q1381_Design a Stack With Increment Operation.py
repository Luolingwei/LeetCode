
# O(1), lazy increment
# 虽然每次要加底部的k个元素，但是实际每次只在要加的第k个元素上加，pop的时候再将相应的inc pop出来加上
# 同时将此时的curinc加到self.inc的末尾，这样累加就会传递给底部的元素

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = []
        self.size = 0
        self.maxsize = maxSize

    def push(self, x: int) -> None:
        if self.size < self.maxsize:
            self.stack.append(x)
            self.inc.append(0)
            self.size += 1

    def pop(self) -> int:
        if self.size == 0: return -1
        curinc = self.inc.pop()
        if self.inc: self.inc[-1] += curinc
        self.size -= 1
        return self.stack.pop() + curinc

    def increment(self, k: int, val: int) -> None:
        k = min(self.size, k)
        if k: self.inc[k - 1] += val


a=CustomStack(2)
a.push(34)
a.increment(8,100)
a.pop()
a.increment(9,91)
a.push(63)
a.pop()
a.push(84)
a.increment(10,93)
a.increment(6,45)
a.increment(10,4)