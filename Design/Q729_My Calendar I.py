import bisect
class MyCalendar:

    def __init__(self):
        self.range=[[float('-inf'),float('-inf')],[float('inf'),float('inf')]]

    def book(self, start: int, end: int):
        # Solution 1
        # for i in range(1,len(self.range)):
        #     if end<=self.range[i][0]:
        #         if start>=self.range[i-1][1]:
        #             self.range.insert(i,[start,end])
        #             return True
        #         else:
        #             return False

        # Solution 2 bisect
        index=bisect.bisect(self.range,[start,end])
        if self.range[index-1][1]<=start and self.range[index][0]>=end:
            bisect.insort(self.range,[start,end])
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(10,20))
print(obj.range)
print(obj.book(15,25))
print(obj.range)
print(obj.book(20,30))
print(obj.range)