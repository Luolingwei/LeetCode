class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid=(len(nums)+1)//2
        nums[::2],nums[1::2]=nums[mid-1::-1],nums[:mid-1:-1]
        return nums


a=Solution()
print(a.wiggleSort([1, 1, 2, 1, 2, 2, 1]))
print(a.wiggleSort([1, 5, 1, 1, 6, 4]))
print(a.wiggleSort([1, 3, 2, 2, 3, 1]))
print(a.wiggleSort([5, 6, 4, 5]))
