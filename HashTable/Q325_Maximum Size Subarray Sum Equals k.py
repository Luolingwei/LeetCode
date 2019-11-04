
# 思路: 只记录leftmost的curS数组，i-memo[curS-k]为以每个数结尾的sumK数组的最大长度

class Solution:
    def maxSubArrayLen(self, nums, k):
        memo={0:-1}
        curS,ans=0,0
        for i,n in enumerate(nums):
            curS+=n
            if curS-k in memo:
                ans=max(ans,i-memo[curS-k])
            if curS not in memo:
                memo[curS]=i
        return ans