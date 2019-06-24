# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

class Solution:
    def findInMountainArray(self, target, mountain_arr):
        # Find the peak
        L=mountain_arr.length()
        l,r=0,L-1
        while l<r:
            mid=(l+r)//2
            if mountain_arr.get(mid)<mountain_arr.get(mid+1):
                l=peak=mid+1
            else:
                r=mid

        # Find in the left
        l,r=0,peak
        while l<=r:
            mid=(l+r)//2
            num=mountain_arr.get(mid)
            if num<target:
                l=mid+1
            elif num>target:
                r=mid-1
            else:
                return mid

        # Find in the right
        l,r=peak,L-1
        while l<=r:
            mid=(l+r)//2
            num=mountain_arr.get(mid)
            if num>target:
                l=mid+1
            elif num<target:
                r=mid-1
            else:
                return mid
        return -1