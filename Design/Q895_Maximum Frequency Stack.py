# Input:
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# Output: [null,null,null,null,null,null,null,5,7,5,4]
# Explanation:
# After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:
#
# pop() -> returns 5, as 5 is the most frequent.
# The stack becomes [5,7,5,7,4].
#
# pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
# The stack becomes [5,7,5,4].
#
# pop() -> returns 5.
# The stack becomes [5,7,4].
#
# pop() -> returns 4.
# The stack becomes [5,7].

# 思路: 分别记录每个元素的频率和每种频率包括的元素，每次pop的时候，pop出最高频率的尾部元素即可(是按顺序加入的)

import collections
class FreqStack:

    def __init__(self):
        self.maxfreq=0
        self.freq=collections.Counter()
        self.stack=collections.defaultdict(list)

    def push(self, x: int) -> None:
        self.freq[x]+=1
        self.maxfreq=max(self.freq[x],self.maxfreq)
        self.stack[self.freq[x]].append(x)

    def pop(self):
        x=self.stack[self.maxfreq].pop()
        if not self.stack[self.maxfreq]: self.maxfreq-=1
        self.freq[x]-=1
        return x


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
obj.pop()
obj.pop()
obj.pop()
obj.pop()