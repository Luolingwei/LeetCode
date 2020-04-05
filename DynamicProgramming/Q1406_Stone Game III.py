
# 思路: 类似Q486(predict the winner)
# dp[i]表示能在以第i个开头的数组中获得的最大差值
# 三种选择，选1个,2个,3个，需要减去dp[i+1],dp[i+2],dp[i+3], 因为下一轮是对手选
# dp[i] = max(arr[i]-dp[i+1],arr[i]+arr[i+1]-dp[i+2],arr[i]+arr[i+1]+arr[i+2]-dp[i+3])
# 初始化dp[-1],dp[-2],dp[-3]即可

class Solution:
    def stoneGameIII(self, arr):
        N = len(arr)
        def helper(n):
             return "Alice" if n>0 else "Bob" if n<0 else "Tie"
        dp=[0]*N
        dp[N-1]=arr[-1]
        if N==1: return helper(dp[0])
        dp[N-2]=max(arr[-2]-arr[-1],arr[-2]+arr[-1])
        if N==2: return helper(dp[0])
        dp[N-3]=max(arr[-3]-dp[N-2],arr[-3]+arr[-2]-dp[N-1],arr[-3]+arr[-2]+arr[-1])
        if N==3: return helper(dp[0])
        for i in range(N-4,-1,-1):
            dp[i] = max(arr[i]-dp[i+1],arr[i]+arr[i+1]-dp[i+2],arr[i]+arr[i+1]+arr[i+2]-dp[i+3])
        return helper(dp[0])

a=Solution()
print(a.stoneGameIII([-1]))
print(a.stoneGameIII([1]))
print(a.stoneGameIII([1,2,3,7]))
print(a.stoneGameIII([1,2,3,-9]))
print(a.stoneGameIII([1,2,3,6]))
print(a.stoneGameIII([1,2,3,-1,-2,-3,7]))
print(a.stoneGameIII([-1,-2,-3]))