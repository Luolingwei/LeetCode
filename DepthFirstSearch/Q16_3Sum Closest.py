class Solution:

    #思路: 和3sum类似, 将数组排序，固定左边的数字i，右边的两个数从i+1到len(nums)-1寻找，如果组合大于0则右边index-1，如果组合小于0则左边index-1,时间复杂度为 0(n^2)
 def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        min=float('inf')
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if abs(s-target)<abs(min-target):
                    min=s
                if s>target:
                    r-=1
                if s<target:
                    l+=1
                if s==target:
                    return min
        return min

a=Solution()
print(a.threeSumClosest([0,9,7,-3,-1,-5,5],10))
print(a.threeSumClosest([-3,-1,2,5],2))
print(a.threeSumClosest([-3,-1,7,5,-4],0))