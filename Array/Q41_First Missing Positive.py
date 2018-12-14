class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 1
        l=len(nums)
        i=1
        while i in nums:
            i+=1
        return i

a=Solution()
print(a.firstMissingPositive([1,2,0]))
print(a.firstMissingPositive([3,4,-1,1]))
print(a.firstMissingPositive([7,8,9,11,12]))
print(a.firstMissingPositive([-2,1,2,4,5]))
print(a.firstMissingPositive([-8,8,-2,2,2]))
print(a.firstMissingPositive([-1,0,1,1,1,2,4]))


