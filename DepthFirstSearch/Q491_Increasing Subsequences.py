# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

# 思路: dfs,不断往后搜索，加入长度大于等于2的升序path
# visited的用法: 在每一个nums中（dfs过程中会出现多个nums, 如4,6,6 | 6,6），如果有重复值出现，如4,6,6，则跳过1个6，因为产生的序列将会全部是重复序列

class Solution:
    def dfs(self,nums,ans,path):
        if len(path)>=2:
            ans.append(path)
        visited=set()
        for i in range(len(nums)):
            if not path or nums[i]>=path[-1]:
                if nums[i] not in visited:
                    visited.add(nums[i])
                    self.dfs(nums[i+1:],ans,path+[nums[i]])

    def findSubsequences(self, nums):
        ans=[]
        self.dfs(nums,ans,[])
        return ans


a=Solution()
print(a.findSubsequences([4,6,6]))
print(a.findSubsequences([4,6,7,7]))