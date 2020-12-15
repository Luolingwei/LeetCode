
# 思路: dp[l][r]表示l到r的数组能获得的最大diff, 每次有2种选择, 拿左边或者右边
# dp[l][r] =  max(getSum(l + 1, r) - dp[l + 1][r], getSum(l, r - 1) - dp[l][r - 1])
# 因为下一次是对方拿, 所以用减号, 双方都optimal play

class Solution:
    def stoneGameVII(self, nums) -> int:

        def getSum(l, r):
            return preS[r] - preS[l - 1]

        N = len(nums)
        preS = nums[:] + [0]
        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            preS[i] += preS[i - 1]

        for gap in range(1, N):
            for l in range(N - gap):
                r = l + gap
                dp[l][r] = max(getSum(l + 1, r) - dp[l + 1][r], getSum(l, r - 1) - dp[l][r - 1])

        return dp[0][N - 1]


a=Solution()
print(a.stoneGameVII([5,3,1,4,2]))
print(a.stoneGameVII([7,90,5,1,100,10,10,2]))