# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# 思路: dp, 每加入一个新的coin，比此coin大的amount的方法数递增dp[i-coin]

class Solution:
    # Solution 1: dfs TLE
    # def change(self, amount, coins):
    #     self.ans=0
    #     def dfs(amount,coins):
    #         if amount<=0:
    #             if amount==0: self.ans+=1
    #             return
    #         for i in range(len(coins)):
    #             dfs(amount-coins[i],coins[i:])
    #     dfs(amount,coins)
    #     return self.ans

    # Solution 2
    def change(self, amount, coins):
        dp=[1]+[0]*amount
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i]+=dp[i-coin]
        return dp[amount]


a=Solution()
print(a.change(5,[1,2,5]))
print(a.change(3,[2]))
print(a.change(10,[10]))