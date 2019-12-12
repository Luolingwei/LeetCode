class Solution(object):
    # solution 1: binary search
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

    # solution 2: Linked List Cycle 2
    # def findDuplicate(self, nums):
    #     slow=fast=finder=0
    #     while True:
    #         slow=nums[slow]
    #         fast=nums[nums[fast]]
    #         if slow==fast:
    #             while finder!=slow:
    #                 slow=nums[slow]
    #                 finder=nums[finder]
    #             return finder

a=Solution()
print(a.findDuplicate([1,3,4,2,2]))
print(a.findDuplicate([1,1,3,4,5]))