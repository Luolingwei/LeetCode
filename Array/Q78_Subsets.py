class Solution:
    #solution1 Iteratively
    # def subsets(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     ans=[[]]
    #     for num in nums:
    #         ans+=[item+[num] for item in ans]
    #     return ans

    #solution2 dfs
    def dfs(self,nums,start,path,ans):
        ans.append(path)
        for i in range(start,len(nums)):
            self.dfs(nums,i+1,path+[nums[i]],ans)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        self.dfs(nums,0,[],ans)
        return ans

a=Solution()
print(a.subsets([1,2,3]))