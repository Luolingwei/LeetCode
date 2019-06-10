# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation:
# For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total you spent $11 and covered all the days of your travel.

# 思路: 注意这里不是cover所有的连续日期，而是只需要cover存在于days的日期.dp[i]记录到达当前日期的最小cost
# 如果非days中的日期直接沿用上一个cost，不需要增加cost；如果出现days中的日期就要考虑在前1,7,30天买票.取最小值

class Solution:
    def mincostTickets(self, days, costs):
        dp,days=[0]*(days[-1]+1),set(days)
        for i in range(1,len(dp)):
            if i not in days: dp[i]=dp[i-1]
            else: dp[i]=min(dp[max(0,i-1)]+costs[0],dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2])
        return dp[-1]

a=Solution()
print(a.mincostTickets([1,4,6,7,8,20],[2,7,15]))
print(a.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31],[2,7,15]))