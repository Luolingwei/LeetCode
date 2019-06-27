# Input: piles = [3,6,7,11], H = 8
# Output: 4

# Input: piles = [30,11,23,4,20], H = 6
# Output: 23

# 思路: binary search, 从1和max(piles)的范围寻找speed
# 如果time>H(超时了，加速): l=mid+1,否则(没超时，还可以更慢),r=mid

import math
class Solution:
    def minEatingSpeed(self, piles, H):
        l,r=1,max(piles)
        while l<r:
            mid=(l+r)//2
            if sum([math.ceil(p/mid) for p in piles])>H:
                l=mid+1
            else:
                r=mid
        return l

a=Solution()
print(a.minEatingSpeed([3,6,7,11],8))
print(a.minEatingSpeed([312884470],968709470))