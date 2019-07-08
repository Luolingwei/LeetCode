# Input:
# nums = [7,2,5,10,8]
# m = 2

# 思路1: dp, dp[i][j]表示前i个数分成j组的最小largest值, dp[i][j]=min(max(dp[k][j-1],sum(nums[k:i])) j-1<=k<=i-1 注意dp[0][0]=0的初始化，否则结果会为inf
# 思路2: binary search，ans的范围是[max(nums),sum(nums)]，对于一个给定上限mid，如果nums被分成多于m个的subarray，l=mid+1，否则，r=mid.

class Solution:
    # Solution 1 dp, TLE
    # def splitArray(self, nums, m):
    #     N=len(nums)
    #     dp=[[float('inf')]*(m+1) for _ in range(N+1)]
    #     dp[0][0]=0
    #     for i in range(1,N+1):
    #         for j in range(1,m+1):
    #             curS=0
    #             for k in range(i-1,j-2,-1):
    #                 curS+=nums[k]
    #                 dp[i][j]=min(dp[i][j],max(dp[k][j-1],curS))
    #     return dp[-1][-1]

    # Solution 2 binary search
    def splitArray(self, nums, m):
        def cal_sub(largest):
            curS,sub=0,1
            for n in nums:
                curS+=n
                if curS>largest:
                    sub+=1
                    curS=n
            return sub

        l,r=max(nums),sum(nums)
        while l<r:
            mid=(l+r)//2
            if cal_sub(mid)>m:
                l=mid+1
            else:
                r=mid
        return l

a=Solution()
print(a.splitArray([7,2,5,10,8],2))