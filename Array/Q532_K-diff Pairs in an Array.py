
# 思路:去重后寻找n+difference是否存在，k=0时需要计算>=2个数的n的个数

import collections
class Solution:
    def findPairs(self, nums, k):
        if k<0: return 0
        if k==0:
            c=collections.Counter(nums)
            return len([n for n in c if c[n]>=2])
        ans=0
        memo=set(nums)
        for n in memo:
            if n+k in memo:
                ans+=1
        return ans

a=Solution()
print(a.findPairs([3, 1, 4, 1, 5],2))
print(a.findPairs([1, 2, 3, 4, 5],1))
print(a.findPairs([1, 3, 1, 5, 4],0))
print(a.findPairs([1, 1, 1, 1, 1],0))
print(a.findPairs([-1, -2, -3],1))