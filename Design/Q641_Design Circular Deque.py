class Node:
    def __init__(self, value):
        self.val = value
        self.pre = self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.tail, self.head = Node(-1), Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.nums = 0
        self.size = k

    def add(self, preNode, val):
        if self.nums < self.size:
            newnode = Node(val)
            newnode.pre = preNode
            newnode.next = preNode.next
            preNode.next = newnode.next.pre = newnode
            self.nums += 1
            return True
        else:
            return False

    def remove(self, preNode):
        if self.nums > 0:
            preNode.next = preNode.next.next
            preNode.next.pre = preNode
            self.nums -= 1
            return True
        else:
            return False

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        return self.add(self.head, value)

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        return self.add(self.tail.pre, value)

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        return self.remove(self.head)

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        return self.remove(self.tail.pre.pre)

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.nums == 0:
            return -1
        return self.head.next.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.nums == 0:
            return -1
        return self.tail.pre.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.nums == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.nums == self.size

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()