class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        big=small=maxnum=nums[0]
        for n in nums[1:]:
            big, small = max(n, n * big, n * small), min(n, n * big, n * small) #记录最大正数和最小负数
            maxnum=max(maxnum,big)
        return maxnum

a=Solution()
print(a.maxProduct([2,3,-2,4]))
print(a.maxProduct([-2,0,-1]))
print(a.maxProduct([-2]))
print(a.maxProduct([-3,2,4,4,2,-2]))
