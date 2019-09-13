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
    # Solution 1 heap
    # def kClosest(self, points,K,A):
    #     return heapq.nsmallest(K,points,key=lambda x:(x[0]-A[0])**2+(x[1]-A[1])**2)

    # Solution 2 sort
    def kClosest(self, points,K,A):
        return sorted(points,key=lambda x:(x[0]-A[0])**2+(x[1]-A[1])**2)[:K]

a=Solution()
print(a.kClosest([[3,3],[1,1]],1,[3,3]))