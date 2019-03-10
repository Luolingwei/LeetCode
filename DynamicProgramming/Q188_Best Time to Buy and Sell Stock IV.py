class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n < 2:
            return 0
        # k is big enougth to cover all ramps.
        if k >= n / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        globalMax = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            # The max profit with i transations and selling stock on day j.
            localMax = [0] * n
            for j in range(1, n):
                profit = prices[j] - prices[j - 1]
                localMax[j] = max(globalMax[i - 1][j - 1] + profit,globalMax[i - 1][j - 1],localMax[j - 1] + profit)
                globalMax[i][j] = max(globalMax[i][j - 1], localMax[j])
        return globalMax[k][-1]

a=Solution()
print(a.maxProfit(2,[3,2,6,5,0,3]))
print(a.maxProfit(2,[3,3,5,0,0,3,1,4]))
print(a.maxProfit(2,[1,2,3,4,5]))
print(a.maxProfit(2,[7,6,4,3,1]))
print(a.maxProfit(3,[1,7,2,5,1,8,9,3]))
print(a.maxProfit(2,[1,2,4,2,5,7,2,4,9,0]))