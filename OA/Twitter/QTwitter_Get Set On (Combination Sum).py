
# Combination Sum, 但只需要判断是否能组合出来，不需要具体组合情况

class Solution:
    def combination(self,nums,target):
        def dfs(nums,target):
            if target<=0:
                return target==0
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                if dfs(nums[i+1:],target-nums[i]):
                    return True
            return False
        nums.sort()
        return dfs(nums,target)

a=Solution()
print(a.combination([2,9,5,1,6],12))
print(a.combination([2,3,15,1,16],8))
print(a.combination([2,3,9,0,2],8))
print(a.combination([8],8))
print(a.combination([],8))