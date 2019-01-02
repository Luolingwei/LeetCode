class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        count=length=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
                length=max(count,length)
            elif nums[i]!=nums[i-1]:
                count=1
        return length

a=Solution()
print(a.longestConsecutive([100, 4, 200, 1, 1, 3, 2]))
print(a.longestConsecutive([0]))
print(a.longestConsecutive([]))
print(a.longestConsecutive([1,2,0,1]))