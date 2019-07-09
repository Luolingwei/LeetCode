# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

# 思路: 无限次交易，一共有三种状态，hold,not_hold,cool，更新各状态的最大值，最后返回not_hold和cool的最大净资产即可.

class Solution:
    def maxProfit(self, prices):
        hold,not_hold,cool=float('-inf'),0,float('-inf')
        for p in prices:
            hold,not_hold,cool=max(hold,not_hold-p),max(not_hold,cool),hold+p
        return max(cool,not_hold)

a=Solution()
print(a.maxProfit([1,2,3,0,2]))