
# 类似find minimum in rotated sorted array

class Solution:
    def findrotate(self,array):
        l,r=0,len(array)-1
        while l<r:
            mid=(l+r)//2
            if array[mid]>array[r]:
                l=mid+1
            else:
                r=mid
        return l

a=Solution()
print(a.findrotate([4,5,6,7,0,1,2]))
print(a.findrotate([2,5,6,0,1,2]))