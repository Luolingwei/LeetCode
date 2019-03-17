class Solution:
    def coinChange(self, coins, amount):
        dp=[0]+[float('inf')]*amount
        for i in range(min(coins),amount+1):
            dp[i]=min([dp[i-coin] for coin in coins if coin<=i])+1
        return dp[amount] if dp[amount]!=float('inf') else -1

a=Solution()
print(a.coinChange([1, 2, 5],11))
print(a.coinChange([2],3))
print(a.coinChange([2],11))
print(a.coinChange([1],0))