class Solution:
    def findKthNum(self, nums1, nums2,k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new_array=[]
        i,j,length=0,0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                new_array.append(nums1[i])
                i,length=i+1,length+1
            else:
                new_array.append(nums2[j])
                j,length=j+1,length+1
            if length==k: return new_array[-1]
        if i==len(nums1):
            return nums2[j+k-length-1]
        if j==len(nums2):
            return nums1[i+k-length-1]

    def findMedianSortedArrays(self, nums1, nums2):
        if (len(nums1)+len(nums2))%2 == 0:
            return (self.findKthNum(nums1,nums2,(len(nums1)+len(nums2))//2)+self.findKthNum(nums1,nums2,(len(nums1)+len(nums2))//2+1))/2
        else:
            return self.findKthNum(nums1,nums2,(len(nums1)+len(nums2))//2+1)

a = Solution()
print(a.findMedianSortedArrays([2,3,5],[5,8,9]))
print(a.findMedianSortedArrays([1,3],[2]))
print(a.findMedianSortedArrays([1,2],[3,4]))









