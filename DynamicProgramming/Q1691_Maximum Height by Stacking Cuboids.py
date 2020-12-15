
# 思路: 题目意思是顺序排列若干三数组合, 求最大的sum
# 先对每个子sublist排序, 然后对整个list排序 (倒序)
# 相对位置固定, 需要选取若干个sublist使得sum最大
# dp[i]表示以i sublist结尾最大可能的sum
# dp[i] = max(dp[0~i] + cuboids[i][0]), 如果i符合条件

class Solution:
    def maxHeight(self, cuboids) -> int:
        N = len(cuboids)
        cuboids = [sorted(c,reverse=True) for c in cuboids]
        cuboids.sort(reverse=True)
        dp = [0]*(N)
        for j in range(N):
            dp[j] = cuboids[j][0]
            for i in range(j):
                if all(cuboids[i][k]>=cuboids[j][k] for k in range(3)):
                    dp[j] = max(dp[j],dp[i]+cuboids[j][0])
        return max(dp)

a=Solution()
print(a.maxHeight([[50,45,20],[95,37,53],[45,23,12]]))
print(a.maxHeight([[38,25,45],[76,35,3]]))
print(a.maxHeight([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]))
print(a.maxHeight([[12,76,13],[68,55,30],[48,85,52],[91,7,41],[29,65,35]]))