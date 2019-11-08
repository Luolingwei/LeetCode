# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2.
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
# Hence, player 1 will never be the winner and you need to return False.
#
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

# 思路: 求最多可能从此数组中得到的数值差，采用bottom-up的dp方法，dp[i][j]=max(nums[left]-dp[left+1][right], nums[right]-dp[left][right-1]).
# 注意是交替挑选数字，所以dp[left+1][right]和dp[left][right-1]表示player2-player1，所以用减号.

class Solution:
    # 1 Find the winner
    def PredictTheWinner(self, nums):
        N = len(nums)
        dp = [[0] * N for _ in range(N)]
        for i in range(N): dp[i][i] = nums[i]

        # for gap in range(1, N):
        #     for l in range(N - gap):
        #         r = l + gap
        #         dp[l][r] = max(nums[l] - dp[l + 1][r], nums[r] - dp[l][r - 1])
        # return dp[0][N - 1] >= 0

        for i in range(N)[::-1]:
            for j in range(i+1,N):
                dp[i][j] = max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])
        return dp[0][N -1] >= 0

    # 2 return the maxScore
    def PredictTheWinner(self, nums):
        N=len(nums)
        dp=[[0]*N for _ in range(N)]
        for i in range(N):
            dp[i][i]=nums[i]
            if i!=N-1: dp[i][i+1]=max(nums[i],nums[i+1])

        # for gap in range(2,N):
        #     for l in range(N-gap):
        #         r=l+gap
        #         dp[l][r]=max(nums[l]+min(dp[l+2][r],dp[l+1][r-1]),nums[r]+min(dp[l+1][r-1],dp[l][r-2]))

        for l in range(N)[::-1]:
            for r in range(l+2,N):
                dp[l][r]=max(nums[l]+min(dp[l+2][r],dp[l+1][r-1]),nums[r]+min(dp[l+1][r-1],dp[l][r-2]))
        return dp[0][N-1]

a=Solution()
print(a.PredictTheWinner([1, 5, 233, 7]))
print(a.PredictTheWinner([1, 5,6, 23,8]))
print(a.PredictTheWinner([1, 5, 2]))
print(a.PredictTheWinner([0]))
print(a.PredictTheWinner([1,3]))