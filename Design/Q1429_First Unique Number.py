from collections import deque
from collections import Counter

# 思路: 用Counter记录当前数组中各个数字的个数
# add的时候如果个数大于0, 那么不需要add进q了, 个数仍累加
# showFirst的时候, 头部个数大于1的直接pop, 避免第二次取的时候又扫描

class FirstUnique:

    def __init__(self, nums):
        self.c = Counter(nums)
        self.q = deque([k for k in self.c.keys() if self.c[k] == 1])

    def showFirstUnique(self) -> int:
        while self.q and self.c[self.q[0]] > 1:
            self.q.popleft()
        if not self.q: return -1
        return self.q[0]

    def add(self, value: int) -> None:
        if self.c[value] == 0:
            self.q.append(value)
        self.c[value] += 1

a=FirstUnique([7,7,7,7,7,7])
print(a.showFirstUnique())
a.add(7)
a.add(3)
a.add(3)
a.add(7)
a.add(17)
print(a.showFirstUnique())