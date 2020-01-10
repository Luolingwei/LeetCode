
# 思路: 对每个index只存储set的值(改变时候的值)
# 对于一个特定的snap_id和index，找到index的序列中([id,val])比它小的id，此val就是该snap_id时的值，因为中间一直未改变

import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[[-1, 0]] for _ in range(length)]
        self.id = 0
        self.L = length

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_right(self.array[index], [snap_id, float('inf')]) - 1
        return self.array[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)