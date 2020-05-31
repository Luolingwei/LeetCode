
# 思路1: 直接将矩阵flatten成deque

# 思路2: 用hasnext()生成有效的row, col的index, 每次next之前进行判断, 使索引有效
# 这种情况可以使任何next都有效

class Vector2D:

    # 思路1
    # def __init__(self, v):
    #     self.memo = deque([n for ln in v for n in ln])
    #
    # def next(self) -> int:
    #     return self.memo.popleft()
    #
    # def hasNext(self) -> bool:
    #     return len(self.memo) > 0


    # 思路2
    def __init__(self, v):
        self.v = v
        self.rowidx = 0
        self.colidx = 0

    def next(self) -> int:
        res = None
        if self.hasNext():
            res = self.v[self.rowidx][self.colidx]
            self.colidx += 1
        return res

    def hasNext(self) -> bool:
        while self.rowidx < len(self.v) and self.colidx == len(self.v[self.rowidx]):
            self.colidx = 0
            self.rowidx += 1
        return self.rowidx != len(self.v)


a=Vector2D([[1,2],[3],[4]])
print(a.next()) # return 1
print(a.next()) # return 2
print(a.next()) # return 3
print(a.hasNext()) # return true
print(a.hasNext()) # return true
print(a.next()) # return 4
print(a.hasNext()) # return false
print(a.next()) # return None
print(a.next()) # return None
print(a.hasNext()) # return false