
# 思路: dp，每一个最大连线数dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+A[i]==B[i])

class Solution:
    def maxUncrossedLines(self, A, B):
        if not A or not B: return 0
        l1,l2=len(A),len(B)
        dp=[[0]*(l2+1) for _ in range(l1+1)]
        for i in range(l1):
            for j in range(l2):
                dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j],dp[i][j]+(A[i]==B[j]))
        return dp[-1][-1]

a=Solution()
print(a.maxUncrossedLines([1,4,2],[1,2,4]))
print(a.maxUncrossedLines([1,3,7,1,7,5],[1,9,2,5,1]))
print(a.maxUncrossedLines([2,5,1,2,5],[10,5,2,1,5,2]))
print(a.maxUncrossedLines([1,1,2,3],[1]))