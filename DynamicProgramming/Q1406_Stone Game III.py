
# 思路: 类似Q486(predict the winner)
# dp[i]表示能在以第i个开头的数组中获得的最大差值
# 三种选择，选1个,2个,3个，需要减去dp[i+1],dp[i+2],dp[i+3], 因为下一轮是对手选
# dp[i] = max(arr[i]-dp[i+1],arr[i]+arr[i+1]-dp[i+2],arr[i]+arr[i+1]+arr[i+2]-dp[i+3])
# 初始化dp[-1],dp[-2],dp[-3]即可

class Solution:

    # 思路1: bottom-up dp
    def stoneGameIII(self, arr) -> str:
        def helper(x):
            return "Alice" if x>0 else "Bob" if x<0 else "Tie"
        N = len(arr)
        dp = [0]*(N+1)
        for i in range(N)[::-1]:
            dp[i], take = float('-inf'), 0
            for k in range(1,4):
                if i+k<=N:
                    take += arr[i+k-1]
                    dp[i] = max(dp[i], take-dp[i+k])
        return helper(dp[0])

    # 思路2: top-down dp
    def stoneGameIII2(self, arr):
        N = len(arr)
        memo = [float('inf')] * N

        def helper(x):
            return "Alice" if x > 0 else "Bob" if x < 0 else "Tie"

        def dp(i):
            if i >= N: return 0
            if memo[i] != float('inf'): return memo[i]
            res, take = float('-inf'), 0
            for k in range(1, 4):
                if i + k <= N:
                    take += arr[i + k - 1]
                    res = max(res, take - dp(i + k))
            memo[i] = res
            return res

        return helper(dp(0))


a=Solution()
print(a.stoneGameIII([-1]))
print(a.stoneGameIII([1]))
print(a.stoneGameIII([1,2,3,7]))
print(a.stoneGameIII([1,2,3,-9]))
print(a.stoneGameIII([1,2,3,6]))
print(a.stoneGameIII([1,2,3,-1,-2,-3,7]))
print(a.stoneGameIII([-1,-2,-3]))