# Input: 1
# Output: 10

# 思路: 每一轮迭代，每个位置上的数字个数等于 sum(上一轮能走到它的数字的方法数)

class Solution:
    def knightDialer(self, N):
        dic=[[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        dp=[1]*10
        for _ in range(N-1):
            dp=[sum(dp[j] for j in dic[i]) for i in range(10)]
        return sum(dp)%(10**9+7)

a=Solution()
print(a.knightDialer(1))
print(a.knightDialer(2))
print(a.knightDialer(3))
print(a.knightDialer(4))