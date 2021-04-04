import bisect

# 思路:
# add range时, 查找left和right对应的index, 如果index是偶数, 是则说明在已有的范围外, 需要用在更新中
# 用slice更新[left, right] / [left] / [right]

# remove range时, 检查index是否是奇数, 是则说明在已有的范围内, 需要用在更新中

# query range时, 检查index是否都是奇数而且相等, 是则说明在同一个范围内, 被cover

class RangeModule:

    def __init__(self):
        self.X = []

    def addRange(self, left: int, right: int) -> None:
        lidx = bisect.bisect_left(self.X, left)
        ridx = bisect.bisect_right(self.X, right)
        sub = []
        if lidx & 1 == 0:
            sub.append(left)
        if ridx & 1 == 0:
            sub.append(right)
        self.X[lidx:ridx] = sub

    def queryRange(self, left: int, right: int) -> bool:
        lidx = bisect.bisect_right(self.X, left)
        ridx = bisect.bisect_left(self.X, right)
        return lidx == ridx and lidx&1

    def removeRange(self, left: int, right: int) -> None:
        lidx = bisect.bisect_left(self.X, left)
        ridx = bisect.bisect_right(self.X, right)
        sub = []
        if lidx & 1 == 1:
            sub.append(left)
        if ridx & 1 == 1:
            sub.append(right)
        self.X[lidx:ridx] = sub


a=RangeModule()
a.addRange(10,20)
a.removeRange(14,16)
print(a.queryRange(10,14))
print(a.queryRange(13,15))
print(a.queryRange(16,17))