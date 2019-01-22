class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([nums[i] for i in range(len(nums)) if i%2==0])

a=Solution()
print(a.arrayPairSum([1,4,3,2]))