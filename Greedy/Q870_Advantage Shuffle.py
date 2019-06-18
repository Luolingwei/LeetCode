# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]

# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]

# 思路: A中比B对应位置大的数才能被保留.
# 将A,B排序，从B的末尾开始check，如果元素b小于a则将A中元素取出来给b.完成后, 如果B中元素如果取到了a则放a，否则放A中剩下的元素.
# 注意可能有重复的元素, 所以dic中要用list存储

import collections
class Solution:
    def advantageCount(self, A, B):
        A.sort()
        dic=collections.defaultdict(list)
        for b in sorted(B)[::-1]:
            if b<A[-1]: dic[b].append(A.pop())
        return [(dic[b] or A).pop() for b in B]

a=Solution()
print(a.advantageCount([2,7,11,15],[1,10,4,11]))
print(a.advantageCount([12,24,8,32],[13,25,32,11]))