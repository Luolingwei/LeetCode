
# 思路: dp[i]表示某个时刻达到总和为i的概率, i可以通过抽取 1~W来达到, 而抽取1~W每个数字又是等概率的
# 所以 i<=K时, dp[i] = sum(dp[i-W:i])/W
# i>K 时, dp[i] = sum(dp[i-W:K])/W, 因为之前可以抽的状态sum只能是<K的
# O(N^2)

# 优化: sliding window记录前W个的dp[i]总和, 注意只记录i<K的dp[i], 因为i大于K之后只能从小于K的dp[i]跳过来
# O(n)

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K==0 or N>=K+W: return 1
        dp = [0]*(N+1)
        dp[0] = 1
        for i in range(1,N+1):
            if i<=K:
                dp[i] = sum(dp[max(0,i-W):i])/W
            else:
                dp[i] = sum(dp[max(0,i-W):K])/W
        return sum(dp[K:])


    def new21Game2(self, N: int, K: int, W: int) -> float:
        if K==0 or N>=K+W: return 1
        dp = [0]*(N+1)
        dp[0] = 1
        curS = 1
        for i in range(1,N+1):
            dp[i] = curS/W
            if i<K: curS += dp[i]
            if i-W>=0: curS -= dp[i-W]
        return sum(dp[K:])


a=Solution()
print(a.new21Game(10,1,10))
print(a.new21Game(6,1,10))
print(a.new21Game(21,17,10))

print(a.new21Game2(10,1,10))
print(a.new21Game2(6,1,10))
print(a.new21Game2(21,17,10))