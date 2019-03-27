class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farest=0
        for i in range(len(nums)):
            if i>farest:
                return False
            farest=max(farest,i+nums[i])
        return True

a = Solution()
print(a.canJump([2,3,1,1,4]))
print(a.canJump([3,2,1,0,4]))
print(a.canJump([2,0]))