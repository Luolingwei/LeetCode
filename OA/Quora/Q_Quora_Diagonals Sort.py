import heapq
import collections
class Solution:
    def sort(self,matrix):
        memo=collections.defaultdict(list)
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                heapq.heappush(memo[i-j],matrix[i][j])
        for i in range(m):
            for j in range(n):
                matrix[i][j]=heapq.heappop(memo[i-j])
        return matrix

a=Solution()
print(a.sort([[8, 4, 1],[4, 4, 1],[4, 8, 9]]))
print(a.sort([[4, 5, 3],[3, 2, 1],[2, 1, 3]]))
print(a.sort([[1, 3, 9, 4 ],[9, 5, 7, 7],[3, 6, 9, 7],[1, 2, 2, 2]]))


