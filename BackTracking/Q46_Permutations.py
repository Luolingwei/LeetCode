class Solution:
    #solution 1
    # def permute(self, nums):
    #     ans=[[]]
    #     for _ in range(len(nums)):
    #         temp=[]
    #         for path in ans:
    #             for num in nums:
    #                 if num not in path: temp.append(path+[num])
    #         ans=temp[:]
    #     return ans

    #solution 2
    # def permute(self, nums):
    #     ans = [[]]
    #     for _ in range(len(nums)):
    #         ans = [path + [num] for path in ans for num in nums if num not in path]
    #     return ans

    #solution 3
    def dfs(self,nums,path,ans):
        if len(path)==len(nums):
            ans.append(path)
            return
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