import heapq
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #solution1
        # nums.sort()
        # return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])

        #solution2
        large,small=heapq.nlargest(3,nums),heapq.nsmallest(2,nums)
        return max(large[0]*large[1]*large[2],small[0]*small[1]*large[0])

a=Solution()
print(a.maximumProduct([1,2,3,4]))
print(a.maximumProduct([1,2,3,-1,-2,-3]))