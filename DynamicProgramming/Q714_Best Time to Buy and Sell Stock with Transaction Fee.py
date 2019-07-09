# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

# 思路: 考虑到只有两种状态: 持有股票hold和不持有股票not_hold，更新两种状态的资产最大值，最后返回not_hold

class Solution:
    def maxProfit(self, prices, fee):
        hold,not_hold=float('-inf'),0
        for p in prices:
            hold=max(hold,not_hold-p-fee)
            not_hold=max(not_hold,hold+p)
        return not_hold

a=Solution()
print(a.maxProfit([1, 3, 2, 8, 4, 9],2))