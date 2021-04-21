from collections import Counter
from sortedcontainers import SortedDict

# 思路: 根据开始时间和结束时间用map记录event增加和减少的数量, 遍历各个时间点, 记录最大的当前event数量
# Python 的sorted Map可以使用SortedDict, Java可以使用TreeMap

class MyCalendarThree:

    def __init__(self):
        self.timeline = Counter()

    def book(self, start: int, end: int) -> int:
        self.timeline[start] += 1
        self.timeline[end] -= 1
        max_event, cur_event = 0, 0
        for t in sorted(self.timeline.keys()):
            cur_event += self.timeline[t]
            max_event = max(max_event, cur_event)
        return max_event


a = MyCalendarThree()
print(a.book(10, 20))
print(a.book(50, 60))
print(a.book(10, 40))
print(a.book(5, 15))
print(a.book(5, 10))
print(a.book(25, 55))


class MyCalendarThree2:

    def __init__(self):
        self.timeline = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.timeline[start] = self.timeline.get(start, 0) + 1
        self.timeline[end] = self.timeline.get(end, 0) - 1
        max_event, cur_event = 0, 0
        for v in self.timeline.values():
            cur_event += v
            max_event = max(max_event, cur_event)
        return max_event


a = MyCalendarThree2()
print(a.book(10, 20))
print(a.book(50, 60))
print(a.book(10, 40))
print(a.book(5, 15))
print(a.book(5, 10))
print(a.book(25, 55))