from functools import lru_cache

# 思路: dp[i][j][k]表示从i(数字个数),j(数字为1-j),k(当前的cost为k)状态到达n,m,k的方法数
# 对于某个状态i,j,k，添加一个数字(1->m), 更新为i+1,newj,newk, ans + dfs[i+1][newj][newk], 总和即为dp[i][j][k]的值
# 用dp进行memo，避免重复dfs
# 如果i>=n表示数字个数已满，停止添加，如果curCost==k则表示符合条件返回1，否则返回0
# 另外如果添加的时候newCost超过了k, 立即停止循环，因为一定不符合条件了

class Solution:
    def numOfArrays(self, n, m, k):
        dp = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
        mod = 10**9+7
        @lru_cache(maxsize=None)
        def dfs(curN,curMax,curCost):
            if curN>=n:
                return curCost==k
            if dp[curN][curMax][curCost]: return dp[curN][curMax][curCost]
            ans=0
            for i in range(1,m+1):
                newMax,newCost = curMax,curCost
                if i>curMax:
                    newCost+=1
                    newMax=i
                if newCost>k: break
                ans=(ans+dfs(curN+1,newMax,newCost))%(mod)
            dp[curN][curMax][curCost]=ans
            return ans
        return dfs(0,0,0)%mod


a=Solution()
print(a.numOfArrays(2,3,1))
print(a.numOfArrays(5,2,3))
print(a.numOfArrays(9,1,1))
print(a.numOfArrays(50,100,25))
print(a.numOfArrays(37,17,7))