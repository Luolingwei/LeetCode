class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #two pointers
        left=right=0
        ans=[]
        while right<len(nums):
            while right+1<len(nums) and nums[right]+1==nums[right+1]:
                right+=1
            if left<right:
                ans.append(str(nums[left])+'->'+str(nums[right]))
            else:
                ans.append(str(nums[left]))
            left,right=right+1,right+1
        return ans

a=Solution()
print(a.summaryRanges([0,1,2,4,5,7]))
print(a.summaryRanges([0,2,3,4,6,8,9]))
print(a.summaryRanges([]))