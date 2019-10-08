
# knapsack问题，每来一个task，更新每个p可能的最大weight，注意要从后往前更新(防止当轮用到更新的p)

class Solution:
    def process(self,tasks,weights,p):
        dp=[0]*(p+1)
        combins=[(2*tasks[i],weights[i]) for i in range(len(tasks))]
        for t,w in combins:
            for i in range(p,-1,-1):
                if i+t<=p:
                    dp[i+t]=max(dp[i+t],dp[i]+w)
        return dp[-1]

a=Solution()
print(a.process([2],[2],4))
print(a.process([2],[2],10))
print(a.process([3,2,2],[3,2,2],9))
print(a.process([2,2,3,4],[2,4,4,5],15))