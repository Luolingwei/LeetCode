class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        num.sort()
        l = len(num)

        if l % 2 != 0:
            return num[int(l / 2)]
        else:
            return (num[int(l / 2)-1] + num[int(l / 2)]) / 2


a = Solution()
print(a.findMedianSortedArrays([7, 9, 8], [1, 3, 2]))









