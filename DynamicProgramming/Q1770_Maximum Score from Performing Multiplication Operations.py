
# 每次可以从左边选或者从右边选，一共有2^m种组合
# 思路1: dfs+memo: dfs(i,l) 表示从当前mults挑选位置为i, nums左边可以挑选的位置为l, 那么右边为l-i-1
# dfs(i,l) = max(dfs(i+1,l+1)+pick_l, dfs(i+1,l)+pick_r), 一共有m^2种dfs(i,l)的组合, bottom-up返回
# O(m^2)

# 思路2: dp, dp[i][j]表示从左边挑选i个并从右边挑选j个所得到的的最大值
# dp[i][j] = max(dp[i-1][j] + pick_l, dp[i][j-1] + pick_r)
# O(m^2)


class Solution:

    def maximumScore1(self, nums, multipliers):
        m = len(multipliers)
        memo = {}
        def dfs(i,l):
            if (i,l) in memo: return memo[(i,l)]
            if i==m: return 0
            pick_l = dfs(i+1,l+1) + nums[l]*multipliers[i]
            pick_r = dfs(i+1,l) + nums[l-i-1]*multipliers[i]
            memo[(i,l)] = max(pick_l,pick_r)
            return memo[(i,l)]
        return dfs(0,0)

    def maximumScore2(self, nums, mults):
        m = len(mults)
        dp = [[0]*(m+1) for _ in range(m+1)]
        res = float('-inf')
        for i in range(m+1):
            for j in range(m-i+1):
                if i+j==0: continue
                pick_left = pick_right = float('-inf')
                if i>0: pick_left = dp[i-1][j] + mults[i+j-1]*nums[i-1]
                if j>0: pick_right = dp[i][j-1] + mults[i+j-1]*nums[-j]
                dp[i][j] = max(pick_left, pick_right)
                if i+j==m: res = max(res, dp[i][j])
        return res


a=Solution()
print(a.maximumScore1([1,2,3],[3,2,1]))
print(a.maximumScore1([-5,-3,-3,-2,7,1],[-10,-5,3,4,6]))
print(a.maximumScore2([1,2,3],[3,2,1]))
print(a.maximumScore2([-5,-3,-3,-2,7,1],[-10,-5,3,4,6]))