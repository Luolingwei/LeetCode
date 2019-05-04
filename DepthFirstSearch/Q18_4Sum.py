class Solution:
    # Solution 1 4Sum using 3Sum
    # def threeSum(self, nums,target):
    #     ans=[]
    #     nums.sort()
    #     for i in range(len(nums)-2):
    #         if i>0 and nums[i]==nums[i-1]:
    #             continue
    #         l,r=i+1,len(nums)-1
    #         while l<r:
    #             s=nums[i]+nums[l]+nums[r]
    #             if s>target:
    #                 r-=1
    #             if s<target:
    #                 l+=1
    #             if s==target:
    #                 ans.append([nums[i],nums[l],nums[r]])
    #                 while l<r and nums[l+1]==nums[l]:
    #                     l+=1
    #                 while l<r and nums[r]==nums[r-1]:
    #                     r-=1
    #                 l+=1; r-=1
    #     return ans
    #
    # def fourSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[List[int]]
    #     """
    #     nums.sort()
    #     ans=[]
    #     for i in range(len(nums)):
    #         if i>0 and nums[i]==nums[i-1]:
    #             continue
    #         ans+=[[nums[i]]+path for path in self.threeSum(nums[i+1:],target-nums[i])]
    #     return ans

    # Solution 2 4 pointers
    def fourSum(self, nums, target):
        x,length=0,len(nums)
        nums.sort()
        ans=[]
        while x<=length-4:
            y=x+1
            while y<=length-3:
                left,right=y+1,length-1
                while left<right:
                    s=nums[x]+nums[y]+nums[left]+nums[right]
                    if s<target:
                        left+=1
                    if s>target:
                        right-=1
                    if s==target:
                        ans.append([nums[x],nums[y],nums[left],nums[right]])
                        while left<right and nums[left+1]==nums[left]:
                            left+=1
                        while left<right and nums[right-1]==nums[right]:
                            right-=1
                        left,right=left+1,right-1
                while y<=length-3 and nums[y+1]==nums[y]:
                    y+=1
                y+=1
            while x<=length-4 and nums[x+1]==nums[x]:
                x+=1
            x+=1
        return ans


a=Solution()
print(a.fourSum([4,7,3,2,-4,2,7,-1],2))
print(a.fourSum([-1,-1,2,-1,-1,2,2,-4,1,-6,5],0))
print(a.fourSum([0,5,9,6,16,12,18,8,-5,-4,-2,-6],3))
print(a.fourSum([1,0,-1,0,-2,2],0))
print(a.fourSum([5,5,3,5,1,-5,1,-2],4))
print(a.fourSum([0,0,0,0],0))