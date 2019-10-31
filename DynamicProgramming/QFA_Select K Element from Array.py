
# dp[i][j]表示从前i个数里选j个的maxSum

class Solution:
    def pickK3(self, nums,k):
        N=len(nums)
        dp=[[float('-inf')]*(k+1) for _ in range(N+1)]
        for i in range(N+1): dp[i][0]=0
        for i in range(1,N+1):
            for j in range(1,k+1):
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+nums[i-1])
        return dp[-1][-1]

a=Solution()
print(a.pickK3([1,2,3],2))
print(a.pickK3([1,6,4,-5,3,2],3))
print(a.pickK3([-1,-6,-4,-5,3,2],4))
print(a.pickK3([-1,-6],3))