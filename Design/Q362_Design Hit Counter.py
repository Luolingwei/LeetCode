import collections

'''
Use a deque to store hits

Evertime we want to getHits, just calculate timestamp-300 as start, and pop all t<=start from queue, return length of deque

'''

class HitCounter:

    # Solution 1 deque
    def __init__(self):
        self.arr = collections.deque()
        self.length = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """

        self.arr.append(timestamp)
        self.length += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        start = timestamp - 300
        while self.arr and self.arr[0] <= start:
            self.arr.popleft()
            self.length -= 1
        return self.length

    # Solution 2 binary search
    # def __init__(self):
    #     self.arr = []
    #     self.length = 0
    #
    # def hit(self, timestamp: int) -> None:
    #     """
    #     Record a hit.
    #     @param timestamp - The current timestamp (in seconds granularity).
    #     """
    #
    #     self.arr.append(timestamp)
    #     self.length += 1
    #
    # def getHits(self, timestamp: int) -> int:
    #     """
    #     Return the number of hits in the past 5 minutes.
    #     @param timestamp - The current timestamp (in seconds granularity).
    #     """
    #     target = timestamp - 300
    #     l, r = 0, self.length - 1
    #     while l < r:
    #         mid = (l + r) // 2
    #         if self.arr[mid] <= target:
    #             l = mid + 1
    #         else:
    #             r = mid
    #     if self.arr and self.arr[l] <= target:
    #         return 0
    #     return self.length - l

obj = HitCounter()
obj.hit(3)
print(obj.getHits(4))