class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps=curr=farest=0
        for i in range(len(nums)-1):
            farest=max(farest,nums[i]+i)
            if i==curr:
                curr=farest
                jumps+=1
            if curr==len(nums)-1:
                break
        return jumps

a = Solution()
print(a.jump([2,3,1,1,4]))
print(a.jump([1,3,5,7,9,11]))