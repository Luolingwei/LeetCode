class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        total=0
        left_price = prices[0]
        right_price = prices[-1]
        left_profit = [0]*len(prices)
        right_profit = [0]*len(prices)
        for i in range(1,len(prices)):
            # total=max(total,self.maxProfit2(prices[:i])+self.maxProfit2(prices[i-1:]))
            left_price = min(left_price, prices[i])
            left_profit[i] = max(prices[i] - left_price, left_profit[i-1])

        for i in range(len(prices)-2,-1,-1):
            right_price = max(right_price, prices[i])
            right_profit[i] = max(right_price-prices[i], right_profit[i+1])

        for i in range(len(prices)):
            total=max(total,left_profit[i]+right_profit[i])

        return total

a=Solution()
print(a.maxProfit([3,3,5,0,0,3,1,4]))
print(a.maxProfit([1,2,3,4,5]))
print(a.maxProfit([7,6,4,3,1]))

