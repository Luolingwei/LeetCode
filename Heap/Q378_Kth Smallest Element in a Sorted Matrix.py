# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.

import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        queue=[]
        heapq.heappush(queue,(matrix[0][0],0,0))
        for _ in range(k):
            value,i,j=heapq.heappop(queue)
            if j==0 and i+1<len(matrix):
                heapq.heappush(queue,(matrix[i+1][j],i+1,j))
            if j+1<len(matrix[0]):
                heapq.heappush(queue,(matrix[i][j+1],i,j+1))
        return value

a=Solution()
print(a.kthSmallest([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],6))

print(a.kthSmallest([
   [ 1,  2],
   [ 1,  3]
],2))