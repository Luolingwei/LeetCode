
# 思路:
# 以target为dp对象, dp[i]表示target为i能组成的最大数字
# 考虑最后一个加进来的数可能为cost数组里的任意一个
# dp[i] = dp[i-c]*10 + (j+1)
# 即将最后一个加进来的数添加到末尾, 取所有可能的最大值即可
# 不可能的target表示为负无穷, 不会对max产生影响

class Solution:
    def largestNumber(self, cost, target):
        dp = [0] + [float('-inf')] * target
        for i in range(1, target + 1):
            for j, c in enumerate(cost):
                if i >= c: dp[i] = max(dp[i], dp[i - c] * 10 + j + 1)
        return str(max(0, dp[target]))

a=Solution()
print(a.largestNumber([4,3,2,5,6,7,2,5,5],9))
print(a.largestNumber([7,6,5,5,5,6,8,7,8],12))
print(a.largestNumber([2,4,6,2,4,6,4,4,4],5))
print(a.largestNumber([2,2,2,5,6,7,3,5,5],9))