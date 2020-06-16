from collections import Counter

# 思路: 先Hash, 从数量少的开始remove, 直到remove掉的数量>=k, 记录remove了多少个元素

class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        c = Counter(arr)
        total, removed, removeE = len(c.values()),0,0
        for n in sorted(c.values()):
            removed,removeE = removed+n,removeE+1
            if removed>=k:
                return total-removeE+(removed!=k)


a=Solution()
print(a.findLeastNumOfUniqueInts([4,3,1,1,3,3,2],3))