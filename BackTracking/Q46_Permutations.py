class Solution:
    def dfs(self,nums,path,ans):
        if len(path)==len(nums):
            ans.append(path)
        for num in nums:
            if num not in path:
                self.dfs(nums,path+[num],ans)
    def permute(self, nums):
        ans=[]
        self.dfs(nums,[],ans)
        return ans

a=Solution()
print(a.permute([1,2]))
print(a.permute([1,2,3]))
print(a.permute([1,2,3,4]))