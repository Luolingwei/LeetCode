
# 思路: memo[i]表示除以3余数为i(0,1,2)的最大sum,每来一个n,更新所有memo[(i+n)%3]的情况, 获得当前3种余数的最大sum情况，最后返回memo[0]

class Solution:
    def maxSumDivThree(self, nums):
        memo=[0,0,0]
        for n in nums:
            new_memo=memo[:]
            for k in memo:
                tail=(k+n)%3
                new_memo[tail]=max(k+n,new_memo[tail])
            memo=new_memo
        return memo[0]

a=Solution()
print(a.maxSumDivThree([3,6,5,1,8]))
print(a.maxSumDivThree([4]))
print(a.maxSumDivThree([1,2,3,4,4]))