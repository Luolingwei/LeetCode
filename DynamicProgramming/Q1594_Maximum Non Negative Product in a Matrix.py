
# dp记录截止到当前点的最大值和最小值即可
# 对于边缘元素, 最大值和最小值相同, 对于中间元素, 分正负进行判断即可
# 若最大值大于等于0则返回

class Solution:
    def maxProductPath(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9+7
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]

        dp[0][0] = [grid[0][0],grid[0][0]]

        for i in range(1,m):
            dp[i][0][0] = dp[i][0][1] = dp[i-1][0][0]*grid[i][0]

        for j in range(1,n):
            dp[0][j][0] = dp[0][j][1] = dp[0][j-1][0]*grid[0][j]

        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] > 0:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0]) * grid[i][j]
                    dp[i][j][1] = min(dp[i - 1][j][1], dp[i][j - 1][1]) * grid[i][j]
                else:
                    dp[i][j][0] = min(dp[i - 1][j][1], dp[i][j - 1][1]) * grid[i][j]
                    dp[i][j][1] = max(dp[i - 1][j][0], dp[i][j - 1][0]) * grid[i][j]

        return dp[-1][-1][0]%mod if dp[-1][-1][0] >=0 else -1


a=Solution()
print(a.maxProductPath([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]))
print(a.maxProductPath([[1,-2,1],[1,-2,1],[3,-4,1]]))