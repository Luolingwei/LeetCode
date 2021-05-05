
# 思路1: dfs+memo (top-down dp), dfs(i) = not any (dfs(i-take)), take = range(1,int(i**0.5)+1)^2
# O(n^1.5)

# 思路2: bottom-up dp, dp[i] = not any(dp[i-take]), take = range(1,int(i**0.5)+1)^2
# O(n^1.5)

class Solution:

    def winnerSquareGame1(self, n):
        memo = [False] + [None]*n
        def dfs(i):
            if memo[i]!=None: return memo[i]
            for base in range(1, int(i**0.5)+1):
                if not dfs(i - base*base):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dfs(n)


    def winnerSquareGame2(self, n):
        dp = [False]*(n+1)
        for i in range(n+1):
            for base in range(1, int(i**0.5)+1):
                if not dp[i-base*base]:
                    dp[i] = True
                    break
        return dp[n]


a=Solution()
print(a.winnerSquareGame1(17))
print(a.winnerSquareGame1(500))

print(a.winnerSquareGame2(17))
print(a.winnerSquareGame2(10000))