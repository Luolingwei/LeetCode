#  Input: [[-2,-3,3],[-5,-10,1],[10,30,-5]]
# Output: 7

# 思路: 倒着考虑，dp[i][j]表示i,j位置至少需要的H值，dp[i][j]=max(1,min(dp[i+1][j],dp[i][j+1])-board[i][j])

class Solution:
    def calculateMinimumHP(self, board):
        m,n=len(board),len(board[0])
        dp=[[float('inf')]*(n+1) for _ in range(m+1)]
        dp[m-1][-1],dp[-1][n-1]=1,1
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                dp[i][j]=max(1,min(dp[i+1][j],dp[i][j+1])-board[i][j])
        return dp[0][0]

a=Solution()
print(a.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
print(a.calculateMinimumHP([[100]]))
print(a.calculateMinimumHP([[1,-4,5,-99],[2,-2,-2,-1]]))