class Solution:
    #solution 1 math
    # def integerBreak(self, n):
    #     x,reminder=divmod(n,3)
    #     if n<4:
    #         return n-1
    #     if reminder==0:
    #         return pow(3,x)
    #     if reminder==1:
    #         return pow(3,x-1)*4
    #     if reminder==2:
    #         return pow(3,x)*2

    #solution2 dp
    def integerBreak(self, n):
        dp=[1]*(n+1)
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i]=max(dp[i],dp[j]*dp[i-j],j*dp[i-j],j*(i-j))
        return dp[n]


a=Solution()
print(a.integerBreak(10))
print(a.integerBreak(2))
print(a.integerBreak(3))
print(a.integerBreak(4))
print(a.integerBreak(19))