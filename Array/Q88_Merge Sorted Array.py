class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)):
            if not nums2:
                break
            if nums1[i]>nums2[0]:
                nums1.insert(i,nums2[0])
                nums1.pop()
                nums2.pop(0)
            elif i+len(nums2)==m+n:
                nums1[i]=nums2.pop(0)
        return nums1

a=Solution()
print(a.merge([1,2,3,0,0,0],3,[2,5,6],3))
print(a.merge([1,2,3,0,0,0,0],3,[1,2,2,100],4))
print(a.merge([2,0],1,[1],1))
print(a.merge([0],0,[1],1))


