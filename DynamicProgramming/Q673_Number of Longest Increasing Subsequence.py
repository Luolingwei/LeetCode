# Similar to Q300
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

# 思路1: dp，dp[i]表示以当前结尾的最长数组.
# 思路2: bisect,以dp记录当前最长递增数组，bisect得到的idx+1为以当前数字n结尾的最长长度 加上长度为idx的比n小个数，最后返回长度为最长个数的总和（以不同数字结尾）.

import bisect
from collections import defaultdict
class Solution:
    # Solution 1 dp 744 ms
    # def findNumberOfLIS(self, nums):
    #     if not nums: return 0
    #     N=len(nums)
    #     dp,dp_count=[1]*N,[1]*N
    #     for i in range(1,N):
    #         for j in range(i):
    #             if nums[i]>nums[j]:
    #                 if dp[j]+1>dp[i]:
    #                     dp[i]=dp[j]+1
    #                     dp_count[i]=dp_count[j]
    #                 elif dp[j]+1==dp[i]:
    #                     dp_count[i]+=dp_count[j]
    #     maxL=max(dp)
    #     return sum(v for u,v in zip(dp,dp_count) if u==maxL)

    # Solution 2 bisect 56 ms
    def findNumberOfLIS(self, nums):
        dp,dic=[],defaultdict(lambda: defaultdict(int))
        for num in nums:
            idx=bisect.bisect_left(dp,num)
            if idx==len(dp):
                dp+=[num]
            else:
                dp[idx]=num
            dic[idx+1][num]+=sum(v for u,v in dic[idx].items() if num>u) if idx>0 else 1
        return sum(dic[len(dp)].values())

a=Solution()
print(a.findNumberOfLIS([10,9,2,5,3,8,101,6,7]))
print(a.findNumberOfLIS([1,3,5,4,7]))
print(a.findNumberOfLIS([1,1,1,1,1]))
print(a.findNumberOfLIS([5,4,3,2,1]))
print(a.findNumberOfLIS([1,2,4,3,5,4,7,2]))