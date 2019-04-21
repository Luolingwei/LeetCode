#只要个数，不要具体构成的数组
class Solution:
    def combinationSum4(self, nums, target):
        nums.sort()
        dp=[1]+[0]*target
        for i in range(1,target+1):
            for n in nums:
                if i-n<0:
                    break
                dp[i]+=dp[i-n]
        return dp[-1]

a=Solution()
print(a.combinationSum4([1, 2, 3],4))
print(a.combinationSum4([1,2,3],0))
print(a.combinationSum4([],0))