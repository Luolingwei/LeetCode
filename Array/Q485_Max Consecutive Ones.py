class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count,length = 0,0
        for num in nums:
            if num:
                count+=1
            else:
                count=0
            if count>length:
                length=count
        return length

a=Solution()
print(a.findMaxConsecutiveOnes([1,1,0,1,1,1]))