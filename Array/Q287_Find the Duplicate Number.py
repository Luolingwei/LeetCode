class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=1
        end=len(nums)-1
        while start<end:
            count = 0
            mid=(start+end)//2
            for number in nums:
                if number<=mid:
                    count+=1
            if count>mid:
                end=mid
            else:
                start=mid+1
        return start

a=Solution()
print(a.findDuplicate([1,3,4,2,2]))