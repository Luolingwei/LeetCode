# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]

# 思路1: 合并后排序
# 思路2: 从后往前, 加入最大的数

class Solution:
    # Solution 1 sort 36 ms
    # def merge(self, nums1, m, nums2, n):
    #     nums1[:]=sorted(nums1[:m]+nums2)

    # Solution two pointers 48 ms
    def merge(self, nums1, m, nums2, n):
        i,j,k=m-1,n-1,m+n-1
        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i,k=i-1,k-1
            else:
                nums1[k]=nums2[j]
                j,k=j-1,k-1
        nums1[:k+1]=nums1[:i+1] or nums2[:j+1]
        return nums1

a=Solution()
print(a.merge([1,2,3,0,0,0],3,[2,5,6],3))
print(a.merge([1,2,3,0,0,0,0],3,[1,2,2,100],4))
print(a.merge([2,0],1,[1],1))
print(a.merge([0],0,[1],1))