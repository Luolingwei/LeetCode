# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

# 思路: 用heap进行排序.比普通sort要快.

import heapq
class Solution:
    def kClosest(self, points,K):
        return heapq.nsmallest(K,points,key=lambda x:x[0]*x[0]+x[1]*x[1])

a=Solution()
print(a.kClosest([[1,3],[-2,2]],1))
print(a.kClosest([[3,3],[5,-1],[-2,4]],2))