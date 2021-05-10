
# 思路1: dp, dp[i]表示以i结尾的子数组能获得的最多sub array个数, dp[i] = max(dp[j](0~i) + sum(j->i) == target)
# 思路2: greedy地生成需要的子数组, 即记录所有preSum, 一旦curS - target 出现, 就可以生成一个子数组, 同时将memo设置成 {curS}
# 意思是所有后面生成的子数组都要从当前curS的位置往后

class Solution:
    def maxNonOverlapping(self, nums, target):
        N = len(nums)
        dp = [0]*(N+1)
        S, minus = 0, 0
        for j in range(1,N+1):
            S += nums[j-1]
            minus = 0
            for i in range(j):
                minus += nums[i-1] if i>0 else 0
                dp[j] = max(dp[j], dp[i] + (S-minus==target))
        return dp[-1]

    def maxNonOverlapping2(self, nums, target):
        res, curS = 0, 0
        memo = {0}
        for n in nums:
            curS += n
            if curS - target in memo:
                res += 1
                memo = {curS}
            memo.add(curS)
        return res


a=Solution()
print(a.maxNonOverlapping([1,1,1,1,1], 2))
print(a.maxNonOverlapping([-1,3,5,1,4,2,-9], 6))
print(a.maxNonOverlapping([-2,6,6,3,5,4,1,2,8], 10))
print(a.maxNonOverlapping([0,0,0], 0))
print(a.maxNonOverlapping2([1,1,1,1,1], 2))
print(a.maxNonOverlapping2([-1,3,5,1,4,2,-9], 6))
print(a.maxNonOverlapping2([-2,6,6,3,5,4,1,2,8], 10))
print(a.maxNonOverlapping2([0,0,0], 0))