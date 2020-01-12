
# 思路: dp[i][j][pos]表示左右finger在i,j位置(字母位置-1-25)，当前需要tap的字母在pos位置，达到最终target所需要的步数
# dp[l][r][pos] = min(dp(next, r, pos + 1) + dist(l, next), dp(l, next, pos + 1) + dist(r, next))
# time complexity: O(27*27*N)

class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(i, j):
            if i == -1:
                return 0
            return abs(i//6-j//6)+abs(i%6-j%6)

        def dp(l, r, pos):
            if pos >= N:
                return 0
            elif memo[l][r][pos] == float('inf'):
                next=ord(word[pos])-ord('A')
                memo[l][r][pos] = min(dp(next, r, pos + 1) + dist(l, next), dp(l, next, pos + 1) + dist(r, next))
            return memo[l][r][pos]

        N = len(word)
        memo = [[[float('inf')]*N for _ in range(27)] for _ in range(27)]
        return dp(-1, -1, 0)

a=Solution()
print(a.minimumDistance("CAKE"))
print(a.minimumDistance("HAPPY"))
print(a.minimumDistance("YEAR"))