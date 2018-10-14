class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        l=len(nums)
        index=None

        while i<l:
            if index==None:
                if nums[i]==target:
                    index=i
                if nums[i]>target:
                    index=i
            else:
                break
            i=i+1

        if index==None:
            index=l

        return index

a=Solution()
print(a.searchInsert([],1))
print(a.searchInsert([1],0))
print(a.searchInsert([1,4,6],7))
print(a.searchInsert([1,3,4,6,7,8,9],5))
print(a.searchInsert([1,2,3,4,5,7,8,9],7))

