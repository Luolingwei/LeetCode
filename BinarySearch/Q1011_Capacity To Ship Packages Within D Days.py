# Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# Output: 15
# Explanation:
# A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# 思路1: dp, dp[i][j]表示第i天运完j个的最小capacity，dp[i][j]=max(dp[i-1][k],sum(weights[k+1:j]))(i-1<=k<j)
# 思路2: binary search, 注意这些数字是要按顺序依次运送的, 通过判断mid是否能满足D天内运送来缩小范围.

class Solution:
    # Solution 1 dp TLE
    # def shipWithinDays(self, weights, D):
    #     dp=[[0]*(len(weights)+1) for _ in range(D+1)]
    #     for j in range(1,len(weights)+1):
    #         dp[1][j]+=dp[1][j-1]+weights[j-1]
    #     for i in range(2,D+1):
    #         for j in range(1,len(weights)+1):
    #             curS,temp=0,float('inf')
    #             for k in range(i-1,j)[::-1]:
    #                 curS+=weights[k]
    #                 temp=min(temp,max(dp[i-1][k],curS))
    #             dp[i][j]=temp
    #     return dp[-1][-1]

    # Solution 2 binary search
    def shipWithinDays(self, weights, D):
        l,r=max(weights),sum(weights)
        while l<r:
            mid,curW,need=(l+r)//2,0,1
            for w in weights:
                if curW+w>mid:
                    need+=1
                    curW=0
                curW+=w
            if need>D:
                l=mid+1
            else: r=mid
        return l

a=Solution()
print(a.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))