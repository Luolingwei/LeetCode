class Solution:
    def dfs(self,nums,path,ans,length):
        if len(path)==length:
            ans.append(path)
            return
        for i in range(len(nums)):
            if i and nums[i]==nums[i-1]:continue
            self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],ans,length)
    def permuteUnique(self, nums):
        nums.sort()
        ans,length=[],len(nums)
        self.dfs(nums,[],ans,length)
        return ans

a=Solution()
print(a.permuteUnique([1,1,2]))
print(a.permuteUnique([1,1,2,2]))