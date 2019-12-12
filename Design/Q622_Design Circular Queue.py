class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [None] * k
        self.size = k
        self.head = 0
        self.tail = 0
        self.nums = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.nums < self.size:
            self.q[self.tail] = value
            self.tail = (self.tail + 1) % self.size
            self.nums += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.nums > 0:
            self.q[self.head] = None
            self.head = (self.head + 1) % self.size
            self.nums -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.nums > 0:
            return self.q[self.head]
        return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.nums > 0:
            return self.q[(self.tail - 1) % self.size]
        return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.nums == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.nums == self.size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()