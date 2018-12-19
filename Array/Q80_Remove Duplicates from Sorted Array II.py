class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        length=count=i=0
        L=len(nums)
        element=nums[0]
        while i<L:
            if nums[i]==element:
                count += 1
            else:
                element = nums[i]
                count=1
            if count<=2:
                length += 1
            else:
                nums.pop(i)
                L-=1
                i-=1
            i+=1
        return length

a=Solution()
print(a.removeDuplicates([0,0,1,1,1,1,2,3,3]))
print(a.removeDuplicates([1,1,1,2,2,3]))


