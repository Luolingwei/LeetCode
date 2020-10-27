
# 思路: score和age大小不能颠倒, 按照age从小到大排序, 从score里面选择sum最大的递增序列即可
# dp[i]表示以i结尾的最大递增sum, dp[i] = max(dp[j(0~i)] + scores[i]) 如果scores[j]<=scores[i]

class Solution:
    def bestTeamScore(self, scores, ages):
        def maxIncrSum(arr):
            dp = arr[:]
            res, n = dp[0], len(arr)
            for i in range(1,n):
                for j in range(i):
                    if arr[j]<=arr[i] and dp[j]+arr[i]>dp[i]:
                        dp[i] = dp[j] + arr[i]
                res = max(res,dp[i])
            return res

        return maxIncrSum([t[1] for t in sorted(zip(ages, scores))])


a=Solution()
print(a.bestTeamScore([1,3,5,10,15],[1,2,3,4,5]))
print(a.bestTeamScore([4,5,6,5],[2,1,2,1]))
print(a.bestTeamScore([1,2,3,5],[8,9,10,1]))