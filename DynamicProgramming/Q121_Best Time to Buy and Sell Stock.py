# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

# 思路: 在第i天卖出的最大利润为 第i天的price-前面的minprice.

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_profit,min_price=0,float('inf')
        for price in prices:
            min_price=min(min_price,price)
            max_profit=max(price-min_price,max_profit)
        return max_profit

a=Solution()
print(a.maxProfit([7,1,5,3,6,4]))
print(a.maxProfit([7,6,4,3,1,0]))
print(a.maxProfit([1,2,3,4,5]))