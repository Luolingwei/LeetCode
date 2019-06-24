# Input: [0,1,0]
# Output: 1

# 思路: 注意这里是寻找target，而不是判断target是否存在，所以二分的判断条件是<, 而不是<=

class Solution:
    def peakIndexInMountainArray(self, A):
        l,r=0,len(A)
        while l<r:
            mid=(l+r)//2
            if A[mid]<A[mid+1]:
                l=mid+1
            else:
                r=mid
        return l

a=Solution()
print(a.peakIndexInMountainArray([1,2,3,4,5,3,1]))