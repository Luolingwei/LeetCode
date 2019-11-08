
# 思路: dp[i][j]表示merge i到j需要的最小cost，对于dp[i][j]，分割为dp[i][k]和dp[k+1][j]，以k-1为步长切割，左右两边都尽量merge，
# 左右两边merge之后最后一步一定一共剩余k个，最后merge一次，加上s[i]...s[j]，返回M[i][j]

class Solution:
    def mergeStones(self, s, K):
        N=len(s)
        if (N-1)%(K-1): return -1
        preS=[0]*(N+1)
        for i in range(1,N+1):
            preS[i]=s[i-1]+preS[i-1]
        M=[[float('inf')] * N for _ in range(N)]
        def dp(i, j):
            if M[i][j]==float('inf'):
                if j-i+1<K:
                    M[i][j] = 0
                else:
                    M[i][j]=min(dp(i, k)+dp(k+1,j) for k in range(i,j ,K-1))
                    if (j-i)%(K-1)==0:
                        M[i][j]+=preS[j+1]-preS[i]
            return M[i][j]
        return dp(0,N-1)

a=Solution()
print(a.mergeStones([3,2,4,1],2))
print(a.mergeStones([3,2,4,1],3))
print(a.mergeStones([3,5,1,2,6],3))
print(a.mergeStones([6,4,4,6],2))