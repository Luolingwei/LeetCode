class Solution:
    def dfs(self,nums,start,target,path,res):
        for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            self.dfs(nums,i+1,target-nums[i],path+[nums[i]],res)
        if target<0:
            return
        if target==0:
            if len(path)==3:
                res.append(path)
                return
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        self.dfs(nums,0,0,[],res)
        return res

a=Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))