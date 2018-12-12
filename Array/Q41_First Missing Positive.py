class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=1
        if nums==[]:
            return 1
        nums.sort()
        l=len(nums)
        if nums[0]>1 or nums[-1]<=0:
            return 1
        while nums[i]<=0:
            i+=1
        while i<l:
            if nums[i]==j:
                    i+=1
                    if i==l:
                        break
                    elif nums[i]!=nums[i-1]:
                        j+=1
            else:
                return j
        if i==l:
            return nums[i-1]+1

a=Solution()
print(a.firstMissingPositive([1,2,0]))
print(a.firstMissingPositive([3,4,-1,1]))
print(a.firstMissingPositive([7,8,9,11,12]))
print(a.firstMissingPositive([-2,1,2,4,5]))
print(a.firstMissingPositive([-8,8,-2,2,2]))
print(a.firstMissingPositive([-1,0,1,1,1,2,4]))


