# Input: piles = [2,7,9,4,4]
# Output: 10

# 思路: dfs, 当前位置i和上限M下Alex能取到的最大的值=S[i]-min(位置i+x能取到的最大值), 其中x从1到2M
# 用memo记录遍历过的结果，减少dfs次数

class Solution:
    def stoneGameII(self, A):
        for i in range(len(A)-2,-1,-1):
            A[i]+=A[i+1]
        memo={}
        def dfs(i,M):
            if (i,M) in memo:
                return memo[(i,M)]
            if i+2*M>=len(A):
                memo[(i,M)]=A[i]
                return A[i]
            memo[(i,M)]=A[i]-min(dfs(i+x,max(M,x)) for x in range(1,2*M+1))
            return memo[(i,M)]
        return dfs(0,1)

a=Solution()
print(a.stoneGameII([2,7,9,4,4]))