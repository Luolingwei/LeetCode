from collections import defaultdict

# 思路: dp[i][y]表示targetPath前i的path联通并以y结尾所需要的最小cost
# dp[i][y] = min(dp[i-1][x]) if x和y联通, 然后再加上y的位置是否需要修正即可(tp[i]!=y)
# pre记录每个dp[i][y]所拿的前面的x, 从dp结果中找到cost最小的结束的node y, 往前倒推x即可找到path

class Solution:
    def mostSimilar(self, n: int, roads, names, tp):
        m = len(tp)
        graph = [[] for _ in range(n)]
        dp = [[float('inf')] * n for _ in range(m)]
        pre = [[-1] * n for _ in range(m)]
        res = [-1] * m

        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)

        for i in range(n):
            dp[0][i] = (tp[0] != names[i])

        for i in range(1, m):
            for y in range(n):
                for x in graph[y]:
                    if dp[i - 1][x] < dp[i][y]:
                        dp[i][y] = dp[i - 1][x]
                        pre[i][y] = x
                dp[i][y] += (tp[i] != names[y])

        res[-1] = min(range(n), key=lambda i: dp[-1][i])
        for k in range(m - 2, -1, -1):
            res[k] = pre[k + 1][res[k + 1]]
        return res


a=Solution()
print(a.mostSimilar(5, [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], ["ATL","PEK","LAX","DXB","HND"], ["ATL","DXB","HND","LAX"]))
print(a.mostSimilar(4, [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], ["ATL","PEK","LAX","DXB"], ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]))
