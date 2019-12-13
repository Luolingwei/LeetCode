from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window=deque()
        self.sum=0
        self.nums=0
        self.cap=size

    def next(self, val: int) -> float:
        if self.nums==self.cap:
            self.sum-=self.window.popleft()
            self.nums-=1
        self.sum+=val
        self.window.append(val)
        self.nums+=1
        return self.sum/self.nums