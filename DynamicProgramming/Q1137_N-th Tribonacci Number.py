# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# 思路: dp解决

class Solution:
    # Solution 1 40 ms
    # def tribonacci(self, n):
    #     dp=[0,1,1]+[0]*(n-2)
    #     for i in range(3,n+1):
    #         dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
    #     return dp[n]

    # Solution 2 36 ms
    def tribonacci(self, n):
        a,b,c=0,1,1
        for _ in range(n):
            a,b,c=b,c,a+b+c
        return a

a=Solution()
print(a.tribonacci(4))
print(a.tribonacci(25))