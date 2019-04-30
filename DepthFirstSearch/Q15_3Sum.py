class Solution:
    # Solution 1: dfs, 311/313 test cases passed
    # def dfs(self,nums,start,target,path,res):
    #     if target<0:
    #         return
    #     if len(path)==3:
    #         if target==0:
    #             res.append(path)
    #         return
    #     for i in range(start,len(nums)):
    #         if i>start and nums[i]==nums[i-1]:
    #             continue
    #         self.dfs(nums,i+1,target-nums[i],path+[nums[i]],res)
    #
    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     res=[]
    #     nums.sort()
    #     self.dfs(nums,0,0,[],res)
    #     return res

    # Solution 2: index from two ends

    # 思路: 将数组排序，固定左边的数字i，右边的两个数从i+1到len(nums)-1寻找，如果组合大于0则右边index-1，如果组合小于0则左边index-1. 时间复杂度 O(n^2) 如果用上述dfs约为O(n^3)
    def threeSum(self, nums):
        ans=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s>0:
                    r-=1
                if s<0:
                    l+=1
                if s==0:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l+1]==nums[l]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1; r-=1
        return ans

a=Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
print(a.threeSum([0,0,0,1,-1]))