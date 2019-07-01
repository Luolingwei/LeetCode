# Example 2:
# Input: poured = 2, query_glass = 1, query_row = 1
# Output: 0.5

# 思路: dp, dp[row]表示当前row的酒量状态, 从第1行一直递推到第query_row行. 下一行的某位置i的酒量等于上一行i和i-1位置的多出来的酒量/2叠加.

class Solution:
    # Solution 1 196 ms
    # def champagneTower(self, poured, query_row, query_glass):
    #     dp=[[0]*(query_row+1) for _ in range(query_row+1)]
    #     dp[0][0]=poured
    #     for row in range(1,query_row+1):
    #         for i in range(row+1):
    #             dp[row][i]=max(0,(dp[row-1][i]-1)/2.0)+max(0,(dp[row-1][i-1]-1)/2.0)
    #     return min(1,dp[query_row][query_glass])

    # Solution 2 172 ms
    def champagneTower(self, poured, query_row, query_glass):
        dp=[poured]+[0]*query_row
        for row in range(1,query_row+1):
            for i in range(row,-1,-1):
                dp[i]=max(0,(dp[i]-1)/2.0)+max(0,(dp[i-1]-1)/2.0)
        return min(1,dp[query_glass])

a=Solution()
print(a.champagneTower(2,1,1))