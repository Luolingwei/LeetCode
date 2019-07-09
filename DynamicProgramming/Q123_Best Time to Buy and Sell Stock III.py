# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

# 思路: 两次交易，一共有四种状态: hold1(持有股票1),not_hold1（已经卖出股票1）,hold2（持有股票2）,not_hold2（已经卖出股票2），更新各个状态的最大值，最后返回not_hold2的剩余资产即可

class Solution:
    def maxProfit(self, prices):
        hold1,hold2,not_hold1,not_hold2=float('-inf'),float('-inf'),0,0
        for p in prices:
            hold1=max(hold1,-p)
            not_hold1=max(not_hold1,hold1+p)
            hold2=max(hold2,not_hold1-p)
            not_hold2=max(not_hold2,hold2+p)
        return not_hold2

a=Solution()
print(a.maxProfit([3,3,5,0,0,3,1,4]))
print(a.maxProfit([1,2,3,4,5]))
print(a.maxProfit([7,6,4,3,1]))