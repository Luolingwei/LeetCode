# Input:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]

# 思路: 根据weight算出preSum, 生成1到total weight的随机整数, 落在哪个index就返回哪个index.
# 每个index对应的整数个数就是该index的weight

import random
import bisect

class Solution:

    def __init__(self, w):
        self.freq = w[:]
        for i in range(1, len(w)):
            self.freq[i] += self.freq[i - 1]
        self.total = self.freq[-1]

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        return bisect.bisect_left(self.freq, x)


a=Solution([1,3])
print(a.pickIndex())
print(a.pickIndex())
print(a.pickIndex())
print(a.pickIndex())
print(a.pickIndex())
print(a.pickIndex())
print(a.pickIndex())
print(a.pickIndex())