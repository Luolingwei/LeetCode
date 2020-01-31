import collections
import heapq

# 思路: 对各对角线用heap存储，然后再次遍历，依次按从小到大pop各对角线

class Solution:
    def diagonalSort(self, mat):
        m,n=len(mat),len(mat[0])
        memo=collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                heapq.heappush(memo[i-j],mat[i][j])
        for i in range(m):
            for j in range(n):
                mat[i][j]=heapq.heappop(memo[i-j])
        return mat

a=Solution()
print(a.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))