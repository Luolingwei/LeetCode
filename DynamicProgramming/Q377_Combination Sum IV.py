# nums = [1, 2, 3]
# target = 4
# Therefore the output is 7.

# 思路: 注意这里是每个数字可以重复使用的，所以dp[target]+=dp[target-n] for n in nums，从1开始到target更新dp

class Solution:

    # 如果是数字不能重复使用,solution as follows:
    # def combinationSum4(self, nums, target):
    #     dp=[1]+[0]*target
    #     for n in nums:
    #         for i in range(target,n-1,-1):
    #             dp[i]+=dp[i-n]
    #     return dp[-1]

    def combinationSum4(self, nums, target):
        dp=[1]+[0]*target
        for i in range(1,target+1):
            for n in nums:
                if i-n>=0:
                    dp[i]+=dp[i-n]
        return dp[-1]


a=Solution()
print(a.combinationSum4([1,2,2,3],4))
print(a.combinationSum4([1,2,3],2))
print(a.combinationSum4([1],2))
print(a.combinationSum4([10,1,2,7,6,5],8))