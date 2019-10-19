# Input: n = 2, rollMax = [1,1,2,2,2,3]
# Output: 34

# 思路:dp[i][j]表示当前轮投出i，i连续出现j次的方法数

class Solution:
    def dieSimulator(self, n, rollMax):
        dp=[[0]*(rollMax[i]+1) for i in range(6)]
        # first round
        for i in range(6):
            dp[i][1]=1
        for _ in range(n-1):
            new_dp=[[0]*(rollMax[i]+1) for i in range(6)]
            total=sum(x for y in dp for x in y)
            for j in range(6):
                for k in range(1,rollMax[j]+1):
                    if k==1:
                        new_dp[j][1]=total-sum(dp[j])
                    else:
                        new_dp[j][k]=dp[j][k-1]
            dp=new_dp
        return sum(n for m in dp for n in m)%(10**9+7)

a=Solution()
print(a.dieSimulator(2,[1,1,2,2,2,3]))
print(a.dieSimulator(2,[1,1,1,1,1,1]))
print(a.dieSimulator(3,[1,1,1,2,2,3]))