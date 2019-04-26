# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

# 思路: DP，动态变化的为数组长度L和分割个数m，dp[L][m]=min(dp[L][m-1],max(dp[i(0->L)][m-1],sum[nums[i:L]])，即每个长度为L的数组分成m份的最优解为: max(长度为 i(0->L) 的数组分为m-1份的最优解, sun(nums[i:L]). 取这个动态得到的最大值的min即可。

class Solution:
    def splitArray(self, nums, m):
        dp=[[float('inf')]*(m+1) for _ in range((len(nums)+1))]
        dp[0][0]=0
        sub=[0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            sub[i]=sub[i-1]+nums[i-1]

        #确定数组长度
        for i in range(1,len(nums)+1):
            #确定分割个数
            for j in range(1,min(i+1,m+1)): #分割个数j不应该超过数组长度i 减少遍历次数
                #动态更新 i长度数组分割j个=max(k(0到i)长度分割j-1个,sum(nums[k:i])
                for k in range(i):
                    dp[i][j]=min(dp[i][j],max(dp[k][j-1],sub[i]-sub[k]))

        return dp[len(nums)][m]

a=Solution()
print(a.splitArray([7,2,5,10,8],2))