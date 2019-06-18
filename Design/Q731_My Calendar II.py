
# 思路: 用两个range分别存储single的和double的范围，每来一个book，分别判断与两个range是否有重叠
# 如果和double的有重叠,return False，如果与single的有重叠，将重叠部分加入double.

class MyCalendarTwo:
    def __init__(self):
        self.single=set()
        self.double=set()
    def book(self, start: int, end: int) -> bool:
        for i,j in self.double:
            if end>i and start<j:
                return False
        for i,j in self.single:
            if end>i and start<j:
                self.double.add((max(i,start),min(j,end)))
        self.single.add((start,end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo()
print(obj.book(10,20))
print(obj.single)
print(obj.double)
print(obj.book(15,25))
print(obj.single)
print(obj.double)
print(obj.book(20,30))
print(obj.single)
print(obj.double)
print(obj.book(15,30))
print(obj.single)
print(obj.double)