class Solution:
    def minMoves2(self, nums):
        nums.sort()
        mid=len(nums)//2
        return nums[mid]*(len(nums)%2==0)+sum(nums[mid+1:])-sum(nums[:mid])