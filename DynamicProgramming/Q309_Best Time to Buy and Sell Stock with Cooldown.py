class Solution:
    def maxProfit(self, prices):
        hold,not_hold_cool,not_hold=float('-inf'),float('-inf'),0
        for price in prices:
            hold,not_hold_cool,not_hold=max(hold,not_hold-price),hold+price,max(not_hold,not_hold_cool)
        return max(not_hold,not_hold_cool)

a=Solution()
print(a.maxProfit([1,2,3,0,2]))