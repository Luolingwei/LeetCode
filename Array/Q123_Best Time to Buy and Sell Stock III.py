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

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total=self.maxProfit(prices)
        for i in range(1,len(prices)):
            total=max(total,self.maxProfit(prices[:i])+self.maxProfit(prices[i:]))
        return total

a=Solution()
print(a.maxProfit2([3,3,5,0,0,3,1,4]))
print(a.maxProfit2([1,2,3,4,5]))
print(a.maxProfit2([7,6,4,3,1]))

