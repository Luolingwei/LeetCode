# Input: nums =
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].

# 思路: dfs+dp，用dp矩阵存储每一个已经计算最长路径的点，避免重复计算

class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]: return 0
        m,n=len(matrix),len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        def dfs(i,j):
            nonlocal m,n
            if not dp[i][j]: #避免重复计算
                dp[i][j]=1
                val=matrix[i][j]
                dp[i][j]+=max(
                    dfs(i+1,j) if i+1<m and matrix[i+1][j]>val else 0,
                    dfs(i-1,j) if i-1>=0 and matrix[i-1][j]>val else 0,
                    dfs(i,j-1) if j-1>=0 and matrix[i][j-1]>val else 0,
                    dfs(i,j+1) if j+1<n and matrix[i][j+1]>val else 0)
            return dp[i][j]
        return max(dfs(i,j) for i in range(m) for j in range(n))

a=Solution()
print(a.longestIncreasingPath([
  [3,4,5],
  [3,2,6],
  [2,2,1]
] ))
print(a.longestIncreasingPath([]))
print(a.longestIncreasingPath([[]]))