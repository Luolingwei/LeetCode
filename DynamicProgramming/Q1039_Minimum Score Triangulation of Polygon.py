# Input: [3,7,4,5]
# Output: 144
# Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.

# 思路: 头部和尾部的两个点一定和某个其他节点形成三角形，dp[i][j](从i到j的最小得分)=min(dp[i][k]+dp[k][j]+A[i]*A[j]*A[k])，k从i+1到j-1，最后返回dp[0][N-1]

class Solution:
    def minScoreTriangulation(self, A):
        N=len(A)
        dp=[[0]*N for _ in range(N)]
        for gap in range(2,N):
            for left in range(N-gap):
                right=left+gap
                dp[left][right]=min(dp[left][k]+dp[k][right]+A[left]*A[k]*A[right] for k in range(left+1,right))
        return dp[0][N-1]

a=Solution()
print(a.minScoreTriangulation([3,7,4,5]))
print(a.minScoreTriangulation([1,3,1,4,1,5]))
print(a.minScoreTriangulation([1,2,3]))