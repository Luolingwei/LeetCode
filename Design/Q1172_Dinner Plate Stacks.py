# Input:
# ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
# [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# Output:
# [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

# 思路: 用一个heap存储可以push的stack的index

import heapq
class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.stack=[]
        self.q=[]

    def push(self, val: int):
        while self.q and self.q[0]<len(self.stack) and len(self.stack[self.q[0]])==self.cap:
            heapq.heappop(self.q)
        if not self.q:
            self.q.append(len(self.stack))
        if self.q[0]==len(self.stack):
            self.stack.append([])
        self.stack[self.q[0]].append(val)

    def pop(self):
        while self.stack and not self.stack[-1]:
            self.stack.pop()
        return self.popAtStack(len(self.stack)-1)

    def popAtStack(self, index: int):
        if 0<=index<len(self.stack) and self.stack[index]:
            heapq.heappush(self.q,index)
            return self.stack[index].pop()
        return -1


# Your DinnerPlates object will be instantiated and called as such:
obj = DinnerPlates(2)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
obj.push(6)
obj.push(7)

print(obj.popAtStack(2))
print(obj.popAtStack(2))
print(obj.popAtStack(1))
print(obj.popAtStack(1))
print(obj.popAtStack(0))

obj.push(8)
obj.push(9)

print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())