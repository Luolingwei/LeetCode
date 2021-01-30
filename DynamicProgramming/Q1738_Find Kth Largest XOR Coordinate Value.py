import heapq

# 思路: XOR [i][j] = matrix[i] ^ XOR [i-1][j-1] ^ XOR [i][j-1] ^ XOR [i-1][j]

class Solution:
    def kthLargestValue(self, matrix, k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        q = []
        for i in range(m):
            for j in range(n):
                if i and j: matrix[i][j]^=matrix[i-1][j-1]
                if i: matrix[i][j]^=matrix[i-1][j]
                if j: matrix[i][j]^=matrix[i][j-1]
                heapq.heappush(q,matrix[i][j])
                if len(q)>k:
                    heapq.heappop(q)
        return heapq.heappop(q)


a=Solution()
print(a.kthLargestValue([[5,2],[1,6]],1))
print(a.kthLargestValue([[5,2],[1,6]],2))
print(a.kthLargestValue([[5,2],[1,6]],3))
print(a.kthLargestValue([[5,2],[1,6]],4))