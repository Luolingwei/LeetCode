
# 思路: same as Q945, there is alternative O(n) solution using counting sort

class Solution:
    # O(nlogn)
    def findUnique(self,nums):
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                nums[i]=nums[i-1]+1
        return sum(nums)

a=Solution()
print(a.findUnique([3,2,1,2,7]))
print(a.findUnique([1,1,1,2]))