# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

# 思路: 用Counter记录各个数字的个数，排序后每来一个数n，n到n+w的个数各减1，如果有哪个数字缺失，则构建失败，返回False.

import collections
class Solution:
    def isNStraightHand(self, hand, W):
        if len(hand)%W: return False
        C=collections.Counter(hand)
        for n in sorted(hand):
            if C[n]:
                for i in range(n,n+W):
                    if not C[i]:return False
                    C[i]-=1
        return True

a=Solution()
print(a.isNStraightHand([1,2,3,6,2,3,4,7,8],3))
print(a.isNStraightHand([1,2,3,4,5,6],2))
print(a.isNStraightHand([3,1,2,2],2))
print(a.isNStraightHand([2,1],2))