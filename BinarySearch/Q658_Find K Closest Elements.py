# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]

# 思路1: 先找到target的位置，然后往两边查找最近的数字.
# 思路2: binary search，查找目标范围的左边界. 取得最近的k个数的时候所有数与x的总距离一定最小.
# 比较A[mid]和x的距离 vs A[mid+k]和x的距离(当前和向右移动一位)
# 如果A[mid]与x距离更大，那么应该范围向右移动查找(l=mid+1)，这样距离一定会变近, 否则保持当前mid为右边界.
# 这样一直往总距离往最小的方向搜索.

import bisect
class Solution:
    # Solution 1 expand from center 160 ms
    # def findClosestElements(self, arr, k, x):
    #     idx=bisect.bisect_left(arr,x)
    #     l,r,ans,count=idx-1,idx,[],0
    #     while l>=0 and r<len(arr) and count<k:
    #         if x-arr[l]<=arr[r]-x:
    #             ans.insert(0,arr[l])
    #             l,count=l-1,count+1
    #         else:
    #             ans.append(arr[r])
    #             r,count=r+1,count+1
    #     if count<k:
    #         if l>=0:ans=arr[l-k+count+1:l+1]+ans
    #         else:ans+=arr[r:r+k-count]
    #     return ans

    # Solution 2 binary search
    def findClosestElements(self, A, k, x):
        l,r=0,len(A)-k
        while l<r:
            mid=(l+r)//2
            if x-A[mid]>A[mid+k]-x:
                l=mid+1
            else:
                r=mid
        return A[l:l+k]

a=Solution()
print(a.findClosestElements([1,2,3,4,5],4,3))
print(a.findClosestElements([1,2,3,4,5],4,-1))
print(a.findClosestElements([3,4,5,10,20],4,5))
print(a.findClosestElements([0,1,2,2,2,3,6,8,8,9],5,9))