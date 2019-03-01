class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit=0
        min_price=prices[0]
        for price in prices:
            min_price=min(min_price,price)
            max_profit=max(price-min_price,max_profit)
        return max_profit

a=Solution()
print(a.maxProfit([7,1,5,3,6,4]))
print(a.maxProfit([7,6,4,3,1,0]))
print(a.maxProfit([1,2,3,4,5]))

