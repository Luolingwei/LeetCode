# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

# 思路: 将所有可以获得的利润累加起来即可.

class Solution:
    def maxProfit(self, prices):
        return sum(max(0,prices[i]-prices[i-1]) for i in range(1,len(prices)))

a=Solution()
print(a.maxProfit([7,1,5,3,6,4]))
print(a.maxProfit([1,2,3,4,5]))
print(a.maxProfit([7,6,4,3,1]))
print(a.maxProfit([]))