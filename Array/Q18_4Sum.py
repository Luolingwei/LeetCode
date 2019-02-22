class Solution:
    def dfs(self,nums,start,target,path,res):
        for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            self.dfs(nums,i+1,target-nums[i],path+[nums[i]],res)
        if target<0:
            return
        if target==0:
            if len(path)==4:
                res.append(path)
                return
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        self.dfs(nums,0,target,[],res)
        return res


a=Solution()
print(a.fourSum([4,7,3,2,-4,2,7,-1],2))
print(a.fourSum([-1,-1,2,-1,-1,2,2,-4,1,-6,5],0))
print(a.fourSum([0,5,9,6,16,12,18,8,-5,-4,-2,-6],3))
print(a.fourSum([1,0,-1,0,-2,2],0))