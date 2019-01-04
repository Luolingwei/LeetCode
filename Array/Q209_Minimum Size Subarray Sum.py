class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left=total=0
        min_length=len(nums)+1
        for right,value in enumerate(nums):
            total+=value
            while total>=s:
                min_length=min(min_length,right-left+1)
                total-=nums[left]
                left+=1
        if min_length<=len(nums):
            return min_length
        else:
            return 0

a=Solution()
print(a.minSubArrayLen(7,[2,3,1,2,4,3]))

