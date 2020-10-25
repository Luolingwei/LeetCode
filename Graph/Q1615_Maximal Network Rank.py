
# 思路: 对于一个pair来说, 与他们相连的edge一定是不同的, 只有pair中的两个点相连的情况才会重复计算一次
# 记录所有点对外的连接情况, check所有的pair, 计算不同的edge数


class Solution:
    def maximalNetworkRank(self, n, roads):
        memo = [set() for _ in range(n)]
        res = 0
        for i,j in roads:
            memo[i].add(j)
            memo[j].add(i)
        for x in range(n):
            for y in range(x+1,n):
                res = max(res, len(memo[x]) + len(memo[y]) - (x in memo[y]))
        return res


a=Solution()
print(a.maximalNetworkRank(4,[[0,1],[0,3],[1,2],[1,3]]))
print(a.maximalNetworkRank(5,[[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]))
print(a.maximalNetworkRank(8,[[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))