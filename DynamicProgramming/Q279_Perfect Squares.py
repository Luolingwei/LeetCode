class Solution:
    #solution 1
    # def numSquares(self, n):
    #     dp=[float('inf')]*(n+1)
    #     for i in range(1,n+1):
    #         if i**0.5==int(i**0.5):
    #             dp[i]=1
    #         else:
    #             dp[i]=min(dp[i-j*j] for j in range(1,int(i**0.5)+1))+1
    #     return dp[-1]

    #solution 2
    def numSquares(self, n):
        dp=[0]
        while len(dp)<n+1:
            dp+=[min(dp[-i*i] for i in range(1,int(len(dp)**0.5)+1))+1]
        return dp[n]

a=Solution()
print(a.numSquares(1))
print(a.numSquares(6))
print(a.numSquares(7))
print(a.numSquares(12))
print(a.numSquares(13))