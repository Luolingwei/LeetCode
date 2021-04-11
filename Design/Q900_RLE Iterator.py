
# 思路1: self.i记录当前index, 每次减去n, 直到越界， next 可能为O(n), 也可能为O(1), 取决于n的大小
# 思路2: binary search, 先存储cumulative count, 对于累加出来的n binary search 对应的数字, next 为O(logn)

import bisect

class RLEIterator:

    def __init__(self, A):
        self.length = len(A)
        self.i = 0
        self.data = A

    def next(self, n: int) -> int:
        while self.i < self.length and self.data[self.i] < n:
            n -= self.data[self.i]
            self.i += 2

        if self.i >= self.length: return -1
        self.data[self.i] -= n
        return self.data[self.i + 1]


a = RLEIterator([3,8,0,9,2,5])
print(a.next(2))
print(a.next(1))
print(a.next(1))
print(a.next(2))


class RLEIterator2:

    def __init__(self, A):
        self.length = len(A)
        self.data = [0]*(self.length//2)
        self.count = [0]*(self.length//2)
        self.n = 0
        for i in range(0,len(A),2):
            self.count[i//2] = A[i] + self.count[i//2-1]
            self.data[i//2] = A[i+1]

    def next(self, n: int) -> int:
        self.n += n
        idx = bisect.bisect_left(self.count, self.n)
        return self.data[idx] if idx<len(self.data) else -1


b = RLEIterator2([3,8,0,9,2,5])
print(b.next(2))
print(b.next(1))
print(b.next(1))
print(b.next(2))